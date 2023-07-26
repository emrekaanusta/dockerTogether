from common.file_reader import file_upload
from services.device_service import (
    read_device,
    add_device,
    update_device,
    delete_device,
    read_all_devices,
)
from models.device import Device


def main():
    print("------Welcome to 'DockerTogether' App------\n")
    print(
        "Please select one of the option:\n"
        "1. Person\n"
        "2. Project\n"
        "3. Device\n"
        "4. Exit\n"
    )
    option = int(input())
    if option > 3:
        print("Good Bye!\n")
        exit(0)

    while option != 4:
        if option == 1:
            
        elif option == 2:
            
        elif option == 3:
            print("1. Read information about devices")
            print("2. Add another device to the database")
            print("3. Delete a device from the database")
            print("4. Update informations of a device")
            print("5. Upload json file to the database\n")

            option = int(input("Please enter your choice: "))
            print(" ")
            checker = False

            while not checker:
                if option == 1:
                    option = int(input("1. Read one device \n2. Read all devices\n"))
                    if option == 1:
                        devicenumber = int(
                            input(
                                "Please enter the device number of the device that you would like to get information about: \n"
                            )
                        )
                        read_device(devicenumber)
                    elif option == 2:
                        read_all_devices()

                elif option == 2:
                    device_num = int(
                        input(
                            "Please enter the device number of the device that you would like to add to the database: "
                        )
                    )
                    ip = input("Please enter the ip number: ")
                    port = input("Please enter the port number: ")
                    username = input("Please enter the username: ")
                    password = input("Please enter the password: ")
                    # TODO input ayrı func
                    device = Device(device_num, ip, port, username, password)
                    add_device(device)

                elif option == 3:
                    number = int(
                        input(
                            "Select the number of the device that you want to delete: "
                        )
                    )
                    delete_device(number)

                elif option == 4:
                    device_num = int(
                        input(
                            "Please enter the device number of the device that you would like to update: "
                        )
                    )
                    update_device(device_num)

                elif option == 5:
                    file_path = input("Enter the path to the JSON file: \n")
                    data = file_upload(file_path, "device_dict")
                    for i in data:
                        value = Device(**i)
                        add_device(value)

                else:
                    checker = True

                print(" ")
                if not checker:
                    option = int(
                        input(
                            "Please enter 1, 2, 3, 4 or 5 to continue database operations and anything other than these to stop the program: "
                        )
                    )

        else:
            print("Good Bye!\n")
            exit(0)


main()
