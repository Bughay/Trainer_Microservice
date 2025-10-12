CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    gender BOOLEAN,
    body_weight INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE food (
    food_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    food_name VARCHAR(255) NOT NULL,
    is_solid BOOLEAN,
    calories_100 DECIMAL NOT NULL,
    protein_100 DECIMAL NOT NULL,
    carbs_100 DECIMAL NOT NULL,
    fats_100 DECIMAL NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipes (
    recipe_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    recipe_name VARCHAR(255) NOT NULL,
    instructions TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipe_ingredients (
    ingredient_id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES recipes(recipe_id),
    food_id INTEGER NOT NULL REFERENCES food(food_id),
    total_grams DECIMAL NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE food_entries (
    nutrition_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ,
    food_id INTEGER REFERENCES food(food_id),
    recipe_id INTEGER REFERENCES recipes(recipe_id),
    calories DECIMAL NOT NULL,
    total_grams DECIMAL NOT NULL,
    protein DECIMAL NOT NULL,
    carbs DECIMAL NOT NULL,
    fats DECIMAL NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);