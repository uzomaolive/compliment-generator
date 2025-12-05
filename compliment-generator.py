import random 
import time

def show_header():
    print("=============================================");
    print("          💛 MOOD-BASED COMPLIMENTS 💛        ");
    print("=============================================");
    print("How are you feeling today?\n");

def show_mood_menu ():
    print("1. Happy 😊");
    print("2. Sad 😢");
    print("3. Angry 😠");
    print("4. Anxious 😰");
    print("5. Excited 🤩");
    print("6. Calm 😌");
    print("7. Exit 🚪");
   
    return input("\nSelect your mood (1-7): ");

# ------------------------
# Mood-specific compliments
# ------------------------

happy_compliments = [
        ]