
def generate_chatbot_training_data(data):
    return {
        "intents": [
            {
        "tag": "greeting",
        "patterns": [
            "Hi", "Hello", "Hey", "Hi there", "Good morning", "Good afternoon",
            "Greetings", "What's up?", "How are you?"
        ],
        "responses": [
            f"Hello {data['user_name']}! Welcome to {data['company_name']}! How can I assist you today?",
            f"Hi there! Excited to help you explore {data['company_name']}!",
            f"Welcome {data['user_name']}! Let me know how I can help you with {data['company_name']}.",
            f"Namaste {data['user_name']}! You're now chatting with {data['company_name']} assistant."
        ]
    },
    {
        "tag": "company_name",
        "patterns": [
            "What is your company name?", 
            "Tell me the name of your company", 
            "Company name?"
        ],
        "responses": [
            f"Our company name is {data['company_name']}.",
            f"We are called {data['company_name']}.",
            f"The name of our company is {data['company_name']}."
        ]
    },
    {
        "tag": "location",
        "patterns": [
            "Where is your company located?", 
            "Company location?",
            "Where are you based?", 
            "Where is your office?"
        ],
        "responses": [
            f"Our company is located in {data['location']}.",
            f"You can find us at {data['location']}.",
            f"We are based in {data['location']}."
        ]
    },
    {
        "tag": "founded_year",
        "patterns": [
            "When was the company founded?", 
            "What is your founding year?",
            "Since when are you operating?", 
            "Founding date?"
        ],
        "responses": [
            f"We were founded in {data['founded_year']}.",
            f"Our company started in {data['founded_year']}.",
            f"We've been operating since {data['founded_year']}."
        ]
    },
            {
                "tag": "about",
                "patterns": [
                  "Tell me about your company", "What do you do?",
                  f"Can you provide details about {data['company_name']}?",
                  f"What is {data['company_name']}?",
                  f"Tell me about {data['company_name']}.",
                  f"Could you describe {data['company_name']}?",
                  f"Details about {data['company_name']}",
                  f"Information on {data['company_name']}",
                  f"Can you give me some information about {data['company_name']}?",
                  f"I'd like some information on {data['company_name']}.",
                  f"Fill me in on {data['company_name']}.",
                  f"Provide some insight into {data['company_name']}.",
                  f"Brief me on {data['company_name']}."
                  ],
                
                "responses": [data["about_company"]]
            },
            {
                "tag": "products_services",
                "patterns": [
                    "What services do you offer?",
                    "Tell me your products and services",
                    "What do you provide?",
                    "List your services",
                    "Can you tell me about your offerings?",
                    "What kind of services do you provide?",
                    "What are your products?",
                    "Tell me about your products and services",
                    "Services you offer?",
                    "What does your company do?",
                    "Do you provide any services?",
                    "I want to know about your services",
                    "What is your business about?",
                    "What type of products do you have?"
                ],
                "responses": [
                    f"We offer {data['product_and_services']}.",
                    f"Our main services include {data['product_and_services']}.",
                    f"We provide the following: {data['product_and_services']}.",
                    f"Our company specializes in {data['product_and_services']}.",
                    f"Here are our services: {data['product_and_services']}.",
                    f"You can get {data['product_and_services']} from us.",
                    f"Our offerings include {data['product_and_services']}.",
                    f"We deliver {data['product_and_services']}.",
                    f"{data['product_and_services']} are the core of our business.",
                    f"Looking for {data['product_and_services']}? We’ve got you covered!"
                ]
            },
            {
                    "tag": "thanks",
                    "patterns": [
                        "Thanks",
                        "Thank you",
                        "Thx",
                        "Thanks a lot",
                        "Many thanks",
                        "Thank you so much",
                        "Thanks for your help",
                        "Thank you very much",
                        "Thanks a ton",
                        "Appreciate it",
                        "Much appreciated"
                    ],
                    "responses": [
                        data["thanks_message"],
                        "You're welcome!",
                        "Glad I could help.",
                        "Happy to help!",
                        "No problem at all.",
                        "Anytime!",
                        "You're most welcome.",
                        "Always here to assist you!",
                        "Thank *you* for reaching out!",
                        "It was my pleasure."
                    ]
                }

        ]
    }
