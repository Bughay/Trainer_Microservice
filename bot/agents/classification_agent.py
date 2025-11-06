from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv('DEEPSEEK_APIKEY')


class ClassificationAgent:
    def __init__(self,api_key,
                 categories,
                 examples):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        self.system_message = f"""Act as a text classification expert. Follow these rules strictly:
                                                                                                           
                    1. Task: Classify the user's text into exactly one of these categories:  
                    {categories}

                    2. Guidelines:  
                    - Respond ONLY with the category name. No explanations.  
                    - If uncertain, choose the closest match.  
                    - Ignore typos/grammar errors. 
                    - Output in JSON format
                    - look clearly at the examples and the JSON format requirement

                    3. Examples (for context):  
                        {examples}"""

    def classify(self,user_message):


        client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_message},
                    {"role": "user", "content": user_message},
                ],
            stream=False,
                    response_format={
                        'type': 'json_object'
                }
            )

        return response.choices[0].message.content


# def test_func():
#     test_questions_dict = {
#         "food": [
#             # 5 questions about food (cooking, recipes, preparation)
#             "What's the best way to cook a perfect medium-rare steak?",
#             "Can you share a simple recipe for homemade tomato sauce?",
#             "How do I make fluffy pancakes from scratch?",
#             "What's a good vegetarian alternative to ground beef in pasta dishes?",
#             "How long should I marinate chicken for maximum flavor?",
            
#             # 5 questions about diet (nutrition, meal planning, dietary advice)
#             "How many grams of protein should I eat daily for muscle building?",
#             "What are some low-carb snack options for weight loss?",
#             "Is intermittent fasting effective for fat loss?",
#             "What foods are high in fiber but low in calories?",
#             "Should I eat before or after my morning workout for optimal results?",
            
#             # 5 food logs (recording meals consumed)
#             "Breakfast: 3 eggs scrambled with spinach, 2 slices bacon, black coffee",
#             "Lunch: grilled chicken breast 6oz, brown rice 1 cup, steamed vegetables 2 cups",
#             "Dinner: baked salmon 8oz, roasted sweet potato, asparagus with lemon",
#             "Snack: Greek yogurt with almonds and honey",
#             "Meal: protein shake with banana and peanut butter after workout"
#         ],
#         "exercise": [
#             # 5 exercise questions
#             "What's the proper form for doing squats to avoid knee pain?",
#             "How many days a week should I workout for optimal muscle growth?",
#             "What exercises are best for building shoulder muscles?",
#             "Should I do cardio before or after weight training?",
#             "How long should I rest between sets for strength training?",
            
#             # 5 exercise logs (recording workouts completed)
#             "Workout: 5x5 squats at 225lbs, 3x10 lunges, 3x15 calf raises",
#             "Cardio: 45 minute run, 5.2 miles, average heart rate 145 bpm",
#             "Gym: bench press 3x8 at 185lbs, pushups 3x15, dumbbell flies 3x12",
#             "Home workout: 30 minute HIIT session, burpees, mountain climbers, jumping jacks",
#             "Training: deadlifts 4x6 at 275lbs, bent over rows 3x10, pullups 3x8"
#         ]
#     }

#     agent = ClassificationAgent(api_key,categories=['food','exercise'],examples=food_classification_examples)
#     correct = 0
#     wrong = 0
#     total = 0
#     for key,value in test_questions_dict.items():
#         for i in range(len(value)):
#             json_result = agent.classify(value[i])
#             json_result = json.loads(json_result)
#             print(value[i])
#             print(json_result['category'])
#             if key == json_result["category"]:
#                 print("correct")
#                 correct +=1
#                 total +=1
#             else:
#                 print("wrong")
#                 wrong +=1
#                 total +=1
#     print(correct, total/correct * 100)
    
            
            
            
            