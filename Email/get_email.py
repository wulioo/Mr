import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


class Email():
    def __init__(self, email, password, pop_server):
        self.email = email
        self.password = password
        self.pop_server = pop_server
        self.get_email()

    def get_email(self):

        # 链接到POP3服务器
        server = poplib.POP3(self.pop_server)

        # 打开调试，打印出会话内容，可选
        server.set_debuglevel(1)

        # 打印POP3服务器的欢迎文字，可选
        print(server.getwelcome().decode('utf-8'))

        # 进行身份认证
        server.user(self.email)
        server.pass_(self.password)


        # stat() 返回邮件数量和占用空间，返回两个。
        mail_total, total_size = server.stat()
        print('Messages: %s. Size: %s' % (mail_total, total_size))
        # print('Messages: %s. Size: %s' % server.stat()).decode('utf-8')

        # list 返回所有邮件编号，第一个是返回状态信息，第二个是列表
        resp, mails, octets = server.list()
        print("邮件列表", mails)
        # 获取最新一封邮件, 注意索引号从1开始,最后是最新的
        index = len(mails)
        # lines存储了邮件的原始文本的每一行,
        resp, lines, octets = server.retr(index)


        # 可以获得整个邮件的原始文本:

        msg_content = b'\r\n'.join(lines).decode('utf-8')
        # 解析成massage对象
        msg = Parser().parsestr(msg_content)
        print(type(msg))  # <class 'email.message.Message'>

        message = msg

        # 关闭连接
        server.quit()

        # 解析邮件正文
        # https://www.cnblogs.com/zixuan-zhang/p/3402821.html
        maintype = message.get_content_maintype()
        if maintype == 'multipart':
            for part in message.get_payload():
                if part.get_content_maintype() == 'text':
                    mail_content = part.get_payload(decode=True).strip()
        elif maintype == 'text':
            mail_content = e.get_payload(decode=True).strip()
        mail_content = mail_content.decode('gbk')
        print(mail_content)



if __name__ == '__main__':
    # 'PRFTIJSKMNMLWLCC',
   e =  Email('a541541000@163.com','PRFTIJSKMNMLWLCC','pop.163.com')
