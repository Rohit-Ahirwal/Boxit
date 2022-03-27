import os
import imaplib
import getpass

os.system('clear')
print('\033[1;92mCreator: Rohit Ahirwal')
os.system('figlet -ctf slant "BOXIT"')
print('Version: 1.0\033[1;0m')

''' User email '''
user_email = input('Emter your email: ')

''' Check email is valid or not '''
if '@gmail.com' in user_email:
    ''' Guide message '''
    print('\033[1;31mWARNING:')
    print('We are now ask password')
    print('Note that we are not use')
    print('gmail password we use google app password')
    print('so enter the google app password')
    print('if you want to know how to get')
    print('google app password')
    print('checkout our github page guide\033[1;0m')
    print('\033[1;68mplease wait we are loading\033[1;0m')
    os.system('sleep 5')

    ''' User Google app password '''
    user_password = getpass.getpass()

    ''' Login using user crendentials '''
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(user_email, user_password)

    ''' Selecting items '''
    imap.select('INBOX')

    ''' Getting message ids '''
    status, get_message = imap.search(None, 'ALL')

    ''' Convert the string ids to list of email ids '''
    messages = get_message[0].split(b' ')

    ''' Working on emails '''
    print('Deleting mails')
    count = 1

    for mail in messages:
        imap.store(mail, '+FLAGS', '\\Deleted')

        if count == 1:
            print(count, 'mail Deleted')
            count += 1
        else:
            print(count, 'mails Deleted')
            count += 1

    print('All selected mail has been deleted')

    ''' Deleting mails '''
    imap.expunge()

    ''' Close gmail '''
    imap.close()

    ''' logout from the server '''
    imap.logout()
else:
    print('Enter valid email address')

