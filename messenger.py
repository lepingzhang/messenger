from wechat_bot import Plugin, Event, register

@register
class MessengerPlugin(Plugin):
    name = "messenger"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.receive_id = self.config.get("receive_id")
        self.send_id = self.config.get("send_id")

    def did_receive_message(self, event: Event):
        # 检查是否是群消息，并且消息文本中是否包含receive_id
        if event.channel.is_group and self.receive_id in event.message.text:
            # 提取消息内容
            msg_to_forward = event.message.text
            
            # 转发消息到send_id
            self.bot.send_txt(self.send_id, msg_to_forward)
            event.bypass()  # 绕过插件链和默认逻辑

    # 实现其他必要的方法
    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "将包含'receive_id'的群消息转发给'send_id'。"
