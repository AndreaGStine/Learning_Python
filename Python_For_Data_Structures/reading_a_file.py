def main():
    #Bad:
    file_1 = open(r"C:\Users\Andrea\Desktop\Programming\Ex_Files_Python_Data_Structures\Exercise_Files\begin_03_03\mazes\modest_maze.txt", "r")
    print(file_1.read())
    file_1.close()

    #Better:
    with open(r"C:\Users\Andrea\Desktop\Programming\Ex_Files_Python_Data_Structures\Exercise_Files\begin_03_03\mazes\modest_maze.txt", "r") as file_1:
        print(file_1.read())


if __name__ == '__main__': main()