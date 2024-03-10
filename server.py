import socket
import threading #we create threads so that no client is waiting if another client has already sent a request, so we use a different thread for a different client

# ------------------ INFORMATION -----------------------

TOTAL_CREDITS = 150
TOTAL_ACADEMIC_CREDITS = 144
TOTAL_NON_ACADEMIC_CREDITS = 6  
TOTAL_FC_CREDITS = 36
TOTAL_CS_CREDITS = 86
TOTAL_OPEN_CREDITS = 22

core_courses = ["P&S", "Linear Algebra", "Calculus", "Physics", "Biology", "Introduction to Computer Science","Discrete Mathematics","Data Structures and Algorithms","Introduction to Machine Learning","Data Science and Management"
,"Theory of Computation"
,"Design and Analysis of Algorithms"
,"Programming Languages and Translation"
,"Information Security"
,"Computer Organisation and Systems"
,"Design Practices in CS"
,"Computer Networks"
,"Embedded Systems"
,"Capstone Project"]

course_plan = [
    "Year 1, Semester 1: Calculus, Introduction to Computer Science, Discrete Mathematics",
    "Year 1, Semester 2: Linear Algebra, Probability and Statistics, Theory of Computation, Computer Organisation and Systems",
    "Year 2, Semester 1: Data Structures and Algorithms, Design Practices in CS",
    "Year 2, Semester 2: Design and Analysis of Algorithms, Data Science and Management, Embedded Systems",
    "Year 3, Semester 1: Introduction to Machine Learning, Computer Networks, Information Security (2 credits)",
    "Year 3, Semester 2: Capstone Project, Programming Languages and Translation",
    "Year 4, Semester 1: ",  # You can add courses for the 4th-year first semester here.
    "Year 4, Semester 2: ",  # You can add courses for the 4th-year second semester here.
]


a1 = f"total number of CS credits required are {TOTAL_CS_CREDITS}"
a2 = f"total CS credits: {TOTAL_CS_CREDITS}. Core courses: 74 credits and Electives: 12 credits."
a3 = f"Core courses are {core_courses}"
a4 = f"Course plan is {course_plan}"
a5 = "Students need to achieve a minimum grade of “B” in both Introduction to Computer Science and Discrete Mathematics courses."
a6 = f"FC credits are {TOTAL_FC_CREDITS}.This includes foundation courses."
a7 = f"A minimum of {TOTAL_NON_ACADEMIC_CREDITS} non-academic credits. They include 4 credits designated for co-curricular courses and 2 credits allocated for internship experience"
a8 = "The pre-requisites of the course 'Introduction to Machine Learning' are 'Data Structures', 'Algorithms', 'Probability and Statistics' and 'Introduction to Computer Science'"
a9 = f"Open credits are {TOTAL_OPEN_CREDITS}. They can be used to take any course from any department, including CS."
a10 = "Insufficient information."
# -------------------- CODE ---------------------------- 

list = ["1: What is the total number of CS credits required to complete the 4-year BSc Hons degree in CS?", "2: Could you provide a breakdown of CS credits?", "3: What are the core courses?", "4: What is the recommended trajectory for the 4 years?", "5: Are there any minimum grade requirements", "6: Explain 'FC credits'", "7: What are 'Non-Academic' Credits?", "8: What are the pre-requisites of the course 'Introduction to Machine Learning'?", "9: How do we use open credits?", "10: Will this degree get me a job?", "0: Exit"]

HEADER  = 64 #size of actual message
FORMAT = 'utf-8'
PORT = 5050
#SERVER = socket.gethostbyname(socket.gethostname()) #gets the ip address of the server on your laptop
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT) #the address of the server to which the client will connect 
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates the socket to connect to the server, AF is the address family which is inet or ipv4 and SOCK_STREAM is the type of socket which is TCP
server.bind(ADDR) #binds the address to the socket, anything that connects to this address now will hit this socket

def handle_client(conn, addr):    #once the server starts and a client is connected, another thread is created for that client and this function is called
    
    print(f"New client connected with address {addr}")
    print(conn.recv(1024).decode(FORMAT))
    #conn.send("Here is the list of questions you can ask: ".encode(FORMAT))
    #conn.send(str(list).encode(FORMAT))
    conn.send("Please enter the question number you want to ask and 0 if you are done: ".encode(FORMAT))

    for i in list:
        conn.send(i.encode(FORMAT))
        conn.send("\n".encode(FORMAT)) 

    while(True):

        

        q = conn.recv(1024).decode(FORMAT)
        if(q == "1"):
            print("q1")
            conn.send(a1.encode(FORMAT))
        elif(q == "2"):
            print("q2")
            conn.send(a2.encode(FORMAT))
        elif(q == "3"):
            print("q3")
            conn.send(a3.encode(FORMAT))
        elif(q == "4"):
            print("q4")
            conn.send(a4.encode(FORMAT))
        elif(q == "5"):
            print("q5")
            conn.send(a5.encode(FORMAT))
        elif(q == "6"):
            print("q6")
            conn.send(a6.encode(FORMAT))
        elif(q == "7"):
            print("q7")
            conn.send(a7.encode(FORMAT))
        elif(q == "8"):
            print("q8")
            conn.send(a8.encode(FORMAT))
        elif(q == "9"):
            print("q9")
            conn.send(a9.encode(FORMAT))
        elif(q == "10"):
            print("q10")
            conn.send(a10.encode(FORMAT))
        elif(q == "0"):
            conn.send("stop".encode(FORMAT))
            break
        else:
            print("Invalid question")
            conn.send("Invalid question".encode(FORMAT))
            break
    
    # while True:
    #     message_size = conn.recv(HEADER).decode(FORMAT)

    #     if(message_size):
    #         message_size = int(message_size)
    #         message = conn.recv(message_size).decode(FORMAT)
    #         if(message == DISCONNECT_MESSAGE):
    #             break
    #         print(f"[{addr}] {message}")   

            
    
    conn.close()



def start():     #this functions will start the server so it starts listening for connection
    server.listen() #listens for connections
    print(f"server is listening on {SERVER}")

    while True:                      #this loop will run forever and will keep listening for connections
        conn, addr = server.accept() #accepts the connection and returns the address and the connection object
        
        thread = threading.Thread(target = handle_client, args = (conn, addr)) #creates a new thread for the client that has connected
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") #prints the number of active connections, -1 because the main thread is also a connection

print("Server is starting...")
start()
server.close()



