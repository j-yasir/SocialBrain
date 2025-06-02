from chains.keyword_extractor import get_trending_keywords
from chains.idea_generator import generate_post_prompts
from chains.post_generator import post_generation

def get_user_input():
    user_input = input("Please enter the topic for your social media post: ")
    num_posts = input("How many posts would you like to generate? ")
    tone = input("What tone would you like for the posts? (e.g., professional, casual, humorous, informative): ")
    if not num_posts.isdigit() or int(num_posts) <= 0:
        print("Invalid input. Please enter a positive integer.")
        return get_user_input()
    return user_input, int(num_posts), tone


def main():
    user_input, num_posts, tone = get_user_input()
    print(f"Generating {num_posts} posts on the topic '{user_input}' with a '{tone}' tone...")
    
  
    
    # For demonstration purposes, we'll just print the inputs
    print(f"User Input: {user_input}")
    print(f"Number of Posts: {num_posts}")
    print(f"Tone: {tone}")
    print("Generating post prompts...")
    
     # extracting trending keywords
    keywords = get_trending_keywords(user_input)
    print(f"Trending Keywords: {keywords}") 


main()