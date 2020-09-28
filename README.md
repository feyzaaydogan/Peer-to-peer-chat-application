# Peer-to-peer-chat-application
P2P chat application in the same LAN using TCP and UDP protocols

Requirements:

    1.  Have 4 processes: ServiceListener, ServiceAdvertiser, ChatListener, ChatClient. Theseprocesses should work as outlined in their respective specifications.
    2.  Successfully detect all available users in the Local Area Network.
    3.  Successfully chat with any available user in the Local Area Network.
    4.  Display an error dialog if a message could not be delivered.
    5.  Output a chat log,  containing timestamps and content of all messages exchanged in achat session.
    
    Logging-in:Upon  connecting  to  the  Local  Area  Network,  P2PC  starts  listening  for  allP2PC services in the LAN. Each detected user is stored in a dictionary.  The end     user isable to display the list of online users.
    
    Sending a message:User can view all available users in the network.  (Implementationdetails for this functionality are to be figured out by the developer.)  The end user           specifiesone username to chat with,  a TCP session is opened with the corresponding IP address,and the user-typed message is encrypted and sent over this TCP connection.           After this,TCP session is closed
    
    Receiving a message:When a new TCP connection request is received, ChatListenerimmediately accepts this connection request and receives, decrypts and displays the mes-sage.       The sender name must be displayed with the message, so that the end user can figureout whom the message is from.
    
    Message history:User can view the message history (information related to chatted user,date/time, and messages).
    
    
