import imaplib

imap_host = 'imap.gmail.com'
imap_user = 'swapnil.tech@global.org.in'
imap_pass = 'Swapnil@1997'

## open a connection 
imap = imaplib.IMAP4_SSL(imap_host)

## login
imap.login(imap_user, imap_pass)

## get status for the mailbox (folder) INBOX
folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")

#print folderStatus

NotReadCounter = str(UnseenInfo[0].split()[2].strip(').,]'))
print NotReadCounter

print "You have "+NotReadCounter+" unread emails"
