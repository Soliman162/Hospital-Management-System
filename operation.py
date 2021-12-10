import json
import os

appointment = ['3AM', '6PM', '5AM', '10AM', '8PM']
department_list = ('DEP_A', 'DEP_B', 'DEP_C', 'DEP_D', 'DEP_E')

#doctor
doctor_file = open("doctor_file.txt", "a")
doctor_file.close()
filesize_doctor = os.path.getsize("doctor_file.txt")

if filesize_doctor == 0:
    doctor_file = open("doctor_file.txt", "w")
    json.dump(dict(), doctor_file)
    doctor_file.close()

doctor_file = open("doctor_file.txt", "r")
data_doctor = doctor_file.read()
doctor_dict = json.loads(data_doctor)
doctor_file.close()

#doctor appoinment
appointment_DOC_file = open("appointment_DOC.txt", "a")
appointment_DOC_file.close()
filesize_appointment_DOC = os.path.getsize("appointment_DOC.txt")

if filesize_appointment_DOC == 0:
    appointment_DOC_file = open("appointment_DOC.txt", "w")
    json.dump(dict(), appointment_DOC_file)
    appointment_DOC_file.close()

appointment_DOC_file = open("appointment_DOC.txt", "r")
data_appointment_DOC = appointment_DOC_file.read()
appointment_DOC = json.loads(data_appointment_DOC)
appointment_DOC_file.close()

#patient
patient_file = open("patient_file.txt", "a")
patient_file.close()
filesize_patient = os.path.getsize("patient_file.txt")

if filesize_patient == 0:
    patient_file = open("patient_file.txt", "w")
    json.dump(dict(), patient_file)
    patient_file.close()

patient_file = open("patient_file.txt", "r")
data_patient = patient_file.read()
patient_dict = json.loads(data_patient)
patient_file.close()

#appointment patient
appointment_patient_file = open("appointment_patient.txt", "a")
appointment_patient_file.close()
filesize_appointment_patient = os.path.getsize("appointment_patient.txt")

if filesize_appointment_patient == 0:
    appointment_patient_file = open("appointment_patient.txt", "w")
    json.dump(dict(), appointment_patient_file)
    appointment_patient_file.close()

appointment_patient_file = open("appointment_patient.txt", "r")
data_appointment_patient = appointment_patient_file.read()
appointment_patient = json.loads(data_appointment_patient)
appointment_patient_file.close()

#patient
def Add_patient (Patient_list):
    patient_dict[Patient_list[9]] = Patient_list[:9]

    patient_file = open("patient_file.txt", "w")
    json.dump(patient_dict, patient_file)
    patient_file.close()

def uniq_patient_id ( Copy_id ):
    for i in range(2):
        for id in patient_dict.keys():
            while Copy_id == id:
                print("repeated id.try again")
                Copy_id = input("please enter the patient's ID: ")
    return Copy_id

def delete_patient(Copy_id):
    flag = 1
    for id in patient_dict.keys():
        if Copy_id == id:
            patient_dict.pop(Copy_id)
            patient_file = open("patient_file.txt", "w")
            json.dump(patient_dict, patient_file)
            patient_file.close()
            flag = 0
            break
    if flag:
        print("ID doesn't exist")

def Edit_patientinfo(Copy_id):

    Dep_0 = input("please enter the name of the department:").upper()
    Doc_1 = input("please enter the name of the doctor following the case:")
    name_2 = input("please enter name of the patient:")
    age_3 = input("please enter age of the patient:")
    gender_4 = input("please enter the gender of the patient:")
    address_5 = input("please enter the address of the patient:")
    number_6 = input("please enter the phone number of the patient:")
    room_7 = input("please enter the room number of the patient:")
    condition_8 = input("please enter the patient's condition:")
    print("*--------------------------------------------------------------*")

    for id in patient_dict.keys():
        if Copy_id == id:
            patient_dict[id][0] = Dep_0
            patient_dict[id][1] = Doc_1
            patient_dict[id][2] = name_2
            patient_dict[id][3] = age_3
            patient_dict[id][4] = gender_4
            patient_dict[id][5] = address_5
            patient_dict[id][6] = number_6
            patient_dict[id][7] = room_7
            patient_dict[id][8] = condition_8
            patient_file = open("patient_file.txt", "w")
            json.dump(patient_dict, patient_file)
            patient_file.close()


def display_patient_info():
    i = 1
    flag = 1
    patient_file = open("patient_file.txt", "r")
    for id in patient_dict.keys():
        print(f"patient number{i}:-")
        print("Department:" + patient_dict[id][0])
        print("Doctor's name:" + patient_dict[id][1])
        print("patient's name:" + patient_dict[id][2])
        print("patient's age:" + patient_dict[id][3])
        print("patient's gender:" + patient_dict[id][4])
        print("patient's address:" + patient_dict[id][5])
        print("patient's number:" + patient_dict[id][6])
        print("patient's room:" + patient_dict[id][7])
        print("patient's condition:" + patient_dict[id][8])
        print("*--------------------------------------------------------------*")
        i += 1
        flag = 0
    if flag:
        print("Empty list")

#doctor

def Add_doctor(doctor_list):
    doctor_dict[doctor_list[4]] = doctor_list[:4]

    for id in doctor_dict.keys():
        name = doctor_dict[id][1]
        appointment_DOC[name] = appointment
    doctor_file = open("doctor_file.txt", "w")
    json.dump(doctor_dict, doctor_file)
    doctor_file.close()

    appointment_DOC_file = open("appointment_DOC.txt", "w")
    json.dump(appointment_DOC, appointment_DOC_file)
    appointment_DOC_file.close()


def uniq_doctor_id(Copy_id):
    for i in range(2):
        for id in doctor_dict.keys():
            while Copy_id == id:
                print("repeated id.try again")
                Copy_id = input("please enter the patient's ID: ")
    return Copy_id


def delete_doctor(Copy_id):
    flag = 1
    for id in doctor_dict.keys():
        if Copy_id == id:
            doctor_dict.pop(Copy_id)
            doctor_file = open("doctor_file.txt", "w")
            json.dump(doctor_dict, doctor_file)
            doctor_file.close()
            flag = 0
            break
    if flag:
        print("ID doesn't exist")


def Edit_doctor_info(Copy_id):

    Dep_0 = input("please enter the name of the department:").upper()
    name_1 = input("please enter the name of the doctor :").upper()
    address_2 = input("please enter the address of the doctor:")
    number_3 = input("please enter the phone number of the patient:")
    print("*--------------------------------------------------------------*")
    for id in doctor_dict.keys():
        if id == Copy_id:
            doctor_dict[Copy_id][0] = Dep_0
            doctor_dict[Copy_id][1] = name_1
            doctor_dict[Copy_id][2] = address_2
            doctor_dict[Copy_id][3] = number_3

            doctor_file = open("doctor_file.txt", "w")
            json.dump(doctor_dict, doctor_file)
            doctor_file.close()
            break

def display_doctor_info():
    i=1
    for id in doctor_dict.keys():
        print(f"doctor number{i}:-")
        print("Department:" + doctor_dict[id][0])
        print("Doctor's name:" + doctor_dict[id][1])
        print("Doctor's address:" + doctor_dict[id][2])
        print("Doctor's number:" + doctor_dict[id][3])
        print("*--------------------------------------------------------------*")
        i += 1

#appointment

def Book_appointment(Copy_id,Copy_appointment):
   for id in patient_dict.keys():
       if id == Copy_id:
           Copy_DOC_name = patient_dict[id][1]
           appointment_patient[Copy_id] = [Copy_DOC_name, Copy_appointment]

           appointment_patient_file = open("appointment_patient.txt", "w")
           json.dump(appointment_patient, appointment_patient_file)
           appointment_patient_file.close()

           for name in appointment_DOC.keys():
                if name == Copy_DOC_name:
                    for i in range(4):
                        if appointment_DOC[name][i] == Copy_appointment:
                            appointment_DOC[name][i] = appointment_DOC[name][i] + " is reserved"

                            appointment_DOC_file = open("appointment_DOC.txt", "w")
                            json.dump(appointment_DOC, appointment_DOC_file)
                            appointment_DOC_file.close()
                            break
                    break
           break

def cancel_appointment(Copy_id):
    for id in patient_dict.keys():
        if id == Copy_id:
            Copy_DOC_name = patient_dict[id][1]
            for name in appointment_DOC.keys():
                if name == Copy_DOC_name:
                    for i in range(4):
                        if appointment_DOC[name][i] == (appointment[i] + " is reserved"):
                            if appointment_patient[Copy_id][1] == appointment[i]:
                                appointment_DOC[name][i] = appointment[i]

                                appointment_DOC_file = open("appointment_DOC.txt", "w")
                                json.dump(appointment_DOC, appointment_DOC_file)
                                appointment_DOC_file.close()
                                break
                    break
    for id in patient_dict.keys():
        if id == Copy_id:
            appointment_patient.pop(Copy_id)

            appointment_patient_file = open("appointment_patient.txt", "w")
            json.dump(appointment_patient, appointment_patient_file)
            appointment_patient_file.close()
            break
            

def Edit_appointment(Copy_id ,Copy_appointment):
    cancel_appointment(Copy_id)
    Book_appointment(Copy_id, Copy_appointment)