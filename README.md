# wechat-gptbot 传令兵插件

本项目作为 `wechat-gptbot` 插件，可以将群聊中@某个id消息转发给另外一个id。

## 安装指南

### 1. 添加插件源
在 `plugins/source.json` 文件中添加以下配置：
```
{
  "messenger": {
    "repo": "https://github.com/lepingzhang/messenger.git",
    "desc": "负责转发群聊消息的传令兵"
  }
}
```

### 2. 插件配置
在 `config.json` 文件中添加以下配置：
```
"plugins": [
  {
    "name": "messenger",
    "receive_id": "被@的昵称",
    "send_id": "wxid_1234567890",
    "room_id_mapping": {
      "1234567890@chatroom": "群聊名称"
    }
  }
]
```
