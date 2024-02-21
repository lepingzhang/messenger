from plugins import register, Plugin, Event
from utils.api import send_txt

@register
class Messenger(Plugin):
    name = "messenger"
    
    def __init__(self, config):
        super().__init__(config)
        self.at_target = "@" + self.config.get("receive_id").lstrip("@")
        self.forward_to_id = self.config.get("send_id")
        self.room_id_mapping = self.config.get("room_id_mapping", {})
        
    def did_receive_message(self, event: Event):
        if event.message.is_group and self.at_target in event.message.content:
            msg_content = event.message.content
            msg_content = msg_content.replace(self.at_target, '').strip()
            sender_name = event.message.sender_name
            room_id = event.message.room_id
            room_name = self.room_id_mapping.get(room_id, room_id)
            msg_to_forward = f"{sender_name}在{room_name}群聊中对您说：\n{msg_content}"
            send_txt(msg_to_forward, self.forward_to_id)
            event.bypass()
        
    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "负责转发群聊消息的传令兵"
