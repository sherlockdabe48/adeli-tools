#!/usr/bin/env python3


def jedi_says(str): 
    """Print the quote of the Jedi. 
    and leave with the famous may the force be with you.
    """
    print(str + ". \n" + "And may the force be with you.")


def japanese_email_content():
    """Print the email content in japanese.
    """
    recipient = input(f"受取人の名前？ > ")
    sender = input(f"あなたの名前？ > ")
    body = input(f"メールの内容を書いてください > ")
    print("----------------------------------------")
    print(f"""
    {recipient}様
          
    いつもお世話になっております。
    ABCの{sender}と申します。
          
    {body}
          
    よろしくお願いいたします。
          
    {sender}
    """)
    print("----------------------------------------")

# japanese_email_content()


def greet(who="Colin"):
    print("Hello,", who)

greet()
