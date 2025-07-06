def copy_file():
   
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the file to write to: ")

    try:
      
        with open(input_file, 'r') as in_file:
            content = in_file.read()
            
            try:
              
                with open(output_file, 'x') as out_file:  # 'x' mode fails if file exists
                    out_file.write(content)
                    print(f"Content successfully copied from '{input_file}' to '{output_file}'")
            
            except FileExistsError:
                print(f"Error: The file '{output_file}' already exists.")
                choice = input("Do you want to overwrite it? (yes/no): ").lower()
                if choice == 'yes':
                    with open(output_file, 'w') as out_file:
                        out_file.write(content)
                        print(f"File '{output_file}' has been overwritten.")
                else:
                    print("Operation cancelled.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


copy_file()