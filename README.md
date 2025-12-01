# Ego Nutrition

A comprehensive, AI-powered health and fitness application that combines nutrition tracking, workout management, recipe planning, and personalized AI coaching and tracking.

# Core Modules
## Module	Description	Key Capabilities
### 🔐 Auth Router	User authentication and authorization system	• JWT-based authentication
• User profile management

• Secure password handling

• TODO: ADD API KEY VERIFICATION FOR Session management

### 🍎 Food Router	Comprehensive nutrition and meal tracking	• Food database with 1000+ items
• Calorie & macro tracking

• Meal logging with timestamps

### 💪 Training Router	Workout and exercise management	• Custom workout creation
• Log and track training

• Data is ready for progress tracking & analytics

### 👨‍🍳 Recipe Router	Smart meal planning and recipes	• Recipe database with nutrition info
• Allows users to create recipee's for future use from the food that they have saved.

• QUICK tracking of means
### 🤖 Agent Router	AI-powered personal coaching	• Personalized meal/workout plans

• Smart AI agent who uses ReAct architecture in order to perform all of this apps services directly through messages

• THIS WILL BE YOUR SMART PERSONAL TRAINER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# tech stack

- FastApi for asynchronous API endpoints

- Postgresql

- Ego_API_tools: https://github.com/Bughay/OpenAI_API_tools my own custom made library that iam working on for AI engineering

- Pydantic  for data validation

- asyncpg for asyncronous raw sql queries 