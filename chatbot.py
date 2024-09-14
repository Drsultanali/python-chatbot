import random
import nltk

# Sample responses for hotel-related queries
responses = {
    "greeting": [
        "Welcome to our hotel! How may I assist you today?",
        "Hello! Thank you for choosing our hotel. How can I help you?",
        "Good day! How can I assist you with your stay today?"
    ],
    "room_availability": [
        "We have several rooms available. What type of room are you looking for?",
        "Yes, we have rooms available. Would you prefer a single or double room?",
        "Our rooms are available for booking. Would you like to make a reservation?"
    ],
    "check_in": [
        "Check-in starts at 2 PM. Can I help you with the process?",
        "You can check in anytime after 2 PM. Let me know if you'd like assistance with early check-in.",
        "Check-in time is 2 PM, but we can accommodate early check-ins based on availability."
    ],
    "check_out": [
        "Check-out time is 11 AM. Will you need any help with your luggage?",
        "Check-out is by 11 AM. Please let us know if you'd like a late check-out.",
        "Our check-out time is 11 AM. Can I assist you with anything else?"
    ],
    "breakfast": [
        "Breakfast is served from 7 AM to 10 AM in the dining area.",
        "We offer a complimentary breakfast from 7 AM to 10 AM.",
        "Breakfast is included in your stay and is served from 7 to 10 AM."
    ],
    "wifi": [
        "Yes, we offer free Wi-Fi. The password is available at the front desk.",
        "Wi-Fi is complimentary for all guests. Would you like the password?",
        "We provide free high-speed Wi-Fi. The password is printed on your room key card."
    ],
    "parking": [
        "Yes, we have free parking available for all guests.",
        "Parking is complimentary and located behind the hotel.",
        "Our hotel offers free parking for guests. Do you need directions to the lot?"
    ],
    "gym": [
        "Our gym is open 24/7. It's located on the first floor near the spa.",
        "We have a fully equipped gym open 24/7 for guests.",
        "The gym is open all day, every day. Can I help you find it?"
    ],
    "pool": [
        "The pool is open from 6 AM to 10 PM daily.",
        "Our pool is heated and available from 6 AM to 10 PM.",
        "You can use the pool anytime between 6 AM and 10 PM."
    ],
    "spa": [
        "Our spa is open from 9 AM to 8 PM. Would you like to book an appointment?",
        "We offer a full-service spa open from 9 AM to 8 PM. Can I assist you with booking?",
        "The spa is available for treatments from 9 AM to 8 PM. Let me know if you’d like to reserve a session."
    ],
    "restaurant": [
        "Our hotel restaurant is open from 12 PM to 10 PM. Would you like a reservation?",
        "The restaurant serves lunch and dinner from noon to 10 PM.",
        "We have a restaurant on-site, open from 12 PM to 10 PM."
    ],
    "room_service": [
        "Room service is available 24/7. What would you like to order?",
        "You can order room service anytime, 24 hours a day.",
        "Our room service is available around the clock. Can I help you place an order?"
    ],
    "laundry": [
        "Yes, we offer laundry services. Would you like to schedule a pick-up?",
        "We have laundry services available. You can leave your laundry at the front desk.",
        "Laundry services are provided daily. Can I assist with your laundry needs?"
    ],
    "airport_shuttle": [
        "Yes, we offer an airport shuttle. It runs every hour. Would you like to reserve a spot?",
        "Our airport shuttle service is complimentary and runs hourly. Shall I reserve a seat for you?",
        "We have an airport shuttle that operates every hour. Let me know if you'd like to book it."
    ],
    "local_attractions": [
        "The local attractions include the city park, museum, and the shopping district. Would you like more information?",
        "There are many attractions nearby, such as the central museum and historic landmarks. Can I help with directions?",
        "We recommend visiting the nearby museum and shopping district. I can provide a map if needed."
    ],
    "unknown": [
        "I'm not sure how to help with that. Could you ask something else?",
        "I didn't understand your request. Could you please rephrase?",
        "Sorry, I don't have information on that. Can I help you with something else?"
    ]
}

# Tokenize user input
def tokenize_input(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    return tokens

# Intent-based response system with hotel-specific queries
def get_response(user_input):
    user_input = user_input.lower()

    # Matching input with known intents
    if any(greeting in user_input for greeting in ['hi', 'hello', 'hey', 'good morning', 'good afternoon']):
        return random.choice(responses["greeting"])
    elif 'room' in user_input or 'availability' in user_input:
        return random.choice(responses["room_availability"])
    elif 'check in' in user_input or 'check-in' in user_input:
        return random.choice(responses["check_in"])
    elif 'check out' in user_input or 'check-out' in user_input:
        return random.choice(responses["check_out"])
    elif 'breakfast' in user_input:
        return random.choice(responses["breakfast"])
    elif 'wifi' in user_input or 'internet' in user_input:
        return random.choice(responses["wifi"])
    elif 'parking' in user_input:
        return random.choice(responses["parking"])
    elif 'gym' in user_input or 'fitness' in user_input:
        return random.choice(responses["gym"])
    elif 'pool' in user_input or 'swimming' in user_input:
        return random.choice(responses["pool"])
    elif 'spa' in user_input:
        return random.choice(responses["spa"])
    elif 'restaurant' in user_input or 'dining' in user_input:
        return random.choice(responses["restaurant"])
    elif 'room service' in user_input or 'food' in user_input:
        return random.choice(responses["room_service"])
    elif 'laundry' in user_input or 'washing' in user_input:
        return random.choice(responses["laundry"])
    elif 'shuttle' in user_input or 'airport' in user_input:
        return random.choice(responses["airport_shuttle"])
    elif 'attractions' in user_input or 'things to do' in user_input:
        return random.choice(responses["local_attractions"])
    else:
        return random.choice(responses["unknown"])

# Main chatbot function
def chatbot():
    print("Chatbot: Welcome to our hotel! How may I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'goodbye']:
            print("Chatbot: Thank you for choosing our hotel. Have a great day!")
            break
        print("Chatbot:", get_response(user_input))

# Run the chatbot
chatbot()
