#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_
# Author: Gaiping Liu gaipingliu@outlook.com

import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()