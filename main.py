from operation import *

print("Hospital Management System")
while(True):
    print("*--------------------------------------------------------------*")
    print("Welcome")
    print("*--------------------------------------------------------------*")

    mode = input("please enter your mode   1-admin or 2-user -->")
    mode = mode.lower()
    if mode == 'admin' or mode == '1':
        for i in range(0, 3):
            print("*--------------------------------------------------------------*")
            pass_word = int(input("please enter your password:"))
            if pass_word == 1234:
                break
            else:
                print("wrong password.please try again\n")
        print("*--------------------------------------------------------------*")

        if pass_word == 1234:
            print("*--------------------------------------------------------------*")
            print("Which of the following would you like to do?")
            print("1-Manage patients")
            print("2-Manage doctors")
            print("3-Book an appointment")
            print("4-Exit")
            print("*--------------------------------------------------------------*")
            choice = input("please enter your choice:").lower()
            if choice == '1' or choice == 'manage patients':
                print("*--------------------------------------------------------------*")
                print("Which of the following would you like to do?")
                print("1- Add patient")
                print("2- Delete patient")
                print("3- Edit patient info")
                print("4- Display patient info")
                print("5- Exit")
                choice = input("please enter your choice:").lower()
                print("*--------------------------------------------------------------*")
                if choice == '1' or choice == 'add patient':
                    info = list()
                    print("*--------------------------------------------------------------*")
                    Dep_0 = (input("please enter the name of the department:")).upper()
                    info.append(Dep_0)
                    Doc_1 = (input("please enter the name of the doctor following the case:")).upper()
                    info.append(Doc_1)
                    name_2 = input("please enter name of the patient:")
                    info.append(name_2)
                    age_3 = input("please enter age of the patient:")
                    info.append(age_3)
                    gender_4 = input("please enter the gender of the patient:")
                    info.append(gender_4)
                    address_5 = input("please enter the address of the patient:")
                    info.append(address_5)
                    number_6 = input("please enter the phone number of the patient:")
                    info.append(number_6)
                    room_7 = input("please enter the room number of the patient:")
                    info.append(room_7)
                    condition_8 = input("please enter the patient's condition:")
                    info.append(condition_8)
                    id_9 = input("please enter the patient's ID: ")
                    id_9 = uniq_patient_id(id_9)
                    info.append(id_9)
                    print("*--------------------------------------------------------------*")
                    Add_patient(info)
                    info.clear()
                elif choice == '2' or choice == 'delete patient':
                    print("*--------------------------------------------------------------*")
                    del_id = input("please enter the patient's ID: ")
                    delete_patient(del_id)
                elif choice == '3' or choice == 'edit patient info':
                    print("*--------------------------------------------------------------*")
                    flag = 0
                    edit_id = input("please enter the patient's ID: ")
                    for id in patient_dict.keys():
                        if id == edit_id:
                            flag = 1
                    if flag:
                        print("*--------------------------------------------------------------*")
                        Edit_patientinfo(edit_id)
                        print("*--------------------------------------------------------------*")
                    else:
                        print("Incorrect ID.")
                        print("*--------------------------------------------------------------*")
                elif choice == '4' or choice == 'display patient info':
                    display_patient_info()
                elif choice == '5' or choice == 'exit':
                    break

            elif choice == '2' or choice == 'manage doctors':
                print("*--------------------------------------------------------------*")
                print("Which of the following would you like to do?")
                print("1- Add doctor")
                print("2- Delete doctor")
                print("3- Edit doctor info")
                print("4- Display doctor info")
                choice = input("please enter your choice:").lower()
                print("*--------------------------------------------------------------*")
                if choice == '1' or choice == 'Add doctor':
                    print("*--------------------------------------------------------------*")
                    info_2 = list()
                    Dep_0 = input("please enter the name of the department:").upper()
                    info_2.append(Dep_0)
                    name_1 = (input("please enter the name of the doctor :")).upper()
                    info_2.append(name_1)
                    address_2 = input("please enter the address of the doctor:")
                    info_2.append(address_2)
                    number_3 = input("please enter the phone number of the doctor:")
                    info_2.append(number_3)
                    id_4 = input("please enter the doctor's ID: ")
                    id_4 = uniq_doctor_id(id_4)
                    info_2.append(id_4)
                    print("*--------------------------------------------------------------*")
                    Add_doctor(info_2)
                    info_2.clear()
                elif choice == '2' or choice == 'delete doctor':
                    print("*--------------------------------------------------------------*")
                    del_id = input("please enter the doctor's ID: ")
                    delete_doctor(del_id)
                elif choice == '3' or choice == 'edit doctor info':
                    flag = 0
                    print("*--------------------------------------------------------------*")
                    edit_id = input("please enter the doctor's ID: ")
                    for id in doctor_dict.keys():
                        if id == edit_id:
                            flag = 1
                    if flag:
                        print("*--------------------------------------------------------------*")
                        Edit_doctor_info(edit_id)
                        print("*--------------------------------------------------------------*")
                    else:
                        print("Incorrect ID.")
                        print("*--------------------------------------------------------------*")
                elif choice == '4' or choice == 'display doctor info':
                    display_doctor_info()
            elif  choice == '3' or choice == 'book an appointment':
                print("*--------------------------------------------------------------*")
                print("Which of the following would you like to do?")
                print("1- Book")
                print("2- Edit")
                print("3- Cancel")
                choice = input("please enter your choice:").lower()
                print("*--------------------------------------------------------------*")
                if choice == '1' or choice == 'book':
                    book_id = input("please enter patient's ID:")
                    flag = 1
                    for id in patient_dict.keys():
                        if id == book_id:
                            flag = 0
                            print("*--------------------------------------------------------------*")
                            Doc_name = patient_dict[book_id][1]
                            if Doc_name in appointment_DOC.keys():
                                    print("The available slots are:-")
                                    print(appointment_DOC[Doc_name][0:])
                                    appointment = input("please enter your appointment: ")
                                    print("*--------------------------------------------------------------*")
                                    Book_appointment(book_id, appointment)
                                    break
                            else:
                                print("Doctor's appointments does not recorded yet")
                    if flag:
                        print("Incorrect ID.")
                        print("*--------------------------------------------------------------*")
                elif choice == '2' or choice == 'edit':
                    Edit_id = input("please enter patient's ID:")
                    flag = 1
                    for id in appointment_patient.keys():
                        if id == Edit_id:
                            Doc_name = patient_dict[Edit_id][1]
                            print("*--------------------------------------------------------------*")
                            print("The available slots are:-")
                            print(appointment_DOC[Doc_name])
                            appointment = input("please enter your appointment: ")
                            print("*--------------------------------------------------------------*")
                            Edit_appointment(Edit_id, appointment)
                            flag = 0
                    if flag:
                        print("Incorrect ID.")
                        print("*--------------------------------------------------------------*")
                elif choice == '3' or choice == 'cancel':
                    print("*--------------------------------------------------------------*")
                    Cancel_id = input("please enter patient's ID:")
                    flag = 1
                    for id in appointment_patient.keys():
                        if id == Cancel_id:
                            cancel_appointment(Cancel_id)
                            flag = 0
                            break
                    if flag:
                        print("Incorrect ID.")
            elif choice == '4' or choice == 'exit':
                break
        else:
            print("system is closed")
            break
    elif mode == 'user' or mode == '2':
        print("*--------------------------------------------------------------*")
        print("Which of the following would you like to do?")
        print("1-View all departments.")
        print("2-View all doctors in a hospital.")
        print("3-View all patients Residents in a hospital.")
        print("4-view patient details.")
        print("5-view appointments.")
        print("6-Exit")
        choice = input("please enter your choice:").lower()
        print("*--------------------------------------------------------------*")
        if choice == '1' or choice == 'view all departments':
            i = 1
            for dep in department_list:
                print(f"{i}-"+dep)
                i += 1
                print("*--------------------------------------------------------------*")
        elif choice == '2' or choice == 'view all doctors in a hospital':
            display_doctor_info()
        elif choice == '3' or choice == 'view all patients Residents in a hospital':
            display_patient_info()
        elif choice == '4' or choice == 'view patient details':
            flag = 1
            print("*--------------------------------------------------------------*")
            ID = input("please enter patient's ID: ")
            for i in patient_dict.keys():
                if ID == i:
                    print("*--------------------------------------------------------------*")
                    print("Department:" + patient_dict[ID][0])
                    print("Doctor's name:" + patient_dict[ID][1])
                    print("patient's name:" + patient_dict[ID][2])
                    print("patient's age:" + patient_dict[ID][3])
                    print("patient's gender:" + patient_dict[ID][4])
                    print("patient's address:" + patient_dict[ID][5])
                    print("patient's number:" + patient_dict[ID][6])
                    print("patient's room:" + patient_dict[ID][7])
                    print("patient's condition:" + patient_dict[ID][8])
                    print("*--------------------------------------------------------------*")
                    flag = 0
                    break
            if flag:
                print("Incorrect ID.")
                print("*--------------------------------------------------------------*")
        elif choice == '5' or choice == 'view appointments':
            flag = 1
            print("*--------------------------------------------------------------*")
            ID = input("please enter Doctor's ID: ")
            print("*--------------------------------------------------------------*")
            for id in doctor_dict.keys():
                if id == ID:
                    Copy_name = doctor_dict[ID][1]
                    print(appointment_DOC[Copy_name])
                    flag = 0
                    break
            print("*--------------------------------------------------------------*")
            if flag:
                print("Incorrect ID.")
                print("*--------------------------------------------------------------*")
        elif choice == '6' or choice == 'exit':
            break