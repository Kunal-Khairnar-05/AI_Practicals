def hospital_expert_system():
    print("--- Medical Diagnosis Expert System ---")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    chest_pain = input("Do you experience chest pain? ").lower()
    rash = input("Do you have a skin rash or itching? ").lower()

    print("\n--- Diagnosis Result ---")
 
    if fever == "yes" and cough == "yes" and chest_pain == "no":
        print("Possible Condition: Common Flu or Viral Infection")
        print("Recommended Department: General Medicine")
        print("Advice: Rest, hydrate, and take over-the-counter fever reducers.")

    elif fever == "yes" and cough == "yes" and chest_pain == "yes":
        print("Possible Condition: Pneumonia or Severe Respiratory Infection")
        print("Recommended Department: Pulmonology (Lungs)")
        print("Advice: Urgent consultation required for a chest X-ray.")

    elif chest_pain == "yes" and fever == "no":
        print("Possible Condition: Potential Heart-related Issue")
        print("Recommended Department: Cardiology")
        print("Advice: Seek immediate medical attention or an ECG.")

    elif rash == "yes":
        if fever == "yes":
            print("Possible Condition: Measles or Chickenpox")
            print("Recommended Department: Infectious Diseases")
        else:
            print("Possible Condition: Allergic Reaction or Dermatitis")
            print("Recommended Department: Dermatology")
        print("Advice: Avoid scratching and apply soothing lotion.")

    elif fever == "yes" and cough == "no" and rash == "no":
        print("Possible Condition: General Fever or Underline Infection")
        print("Recommended Department: General Physician")
        print("Advice: Monitor your temperature and stay hydrated.")

    else:
        print("Condition: Symptoms inconclusive.")
        print("Recommended Department: Outpatient Department (OPD)")
        print("Advice: Please consult a general doctor for a full check-up.")

hospital_expert_system()