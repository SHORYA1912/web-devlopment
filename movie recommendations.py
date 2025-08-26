import pandas as pd
from textblob import TextBlob

movies_df = pd.read_csv('imdb_top_1000.csv')



print("Welcome to Movie Recommender!")

def recommend_movies_debug(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df

    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    print(f"After genre filter: {len(filtered_df)} movies")

    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]
    print(f"After rating filter: {len(filtered_df)} movies")

    mood_polarity = TextBlob(mood).sentiment.polarity if mood else None

    recommendations = []
    for _, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity

        # Relaxed mood filter: difference less than 0.7 (adjustable)
        if mood and abs(mood_polarity - polarity) > 0.7:
            continue

        recommendations.append((row['Series_Title'], polarity))
        if len(recommendations) == top_n:
            break

    print(f"Movies after mood filter: {len(recommendations)}")
    return recommendations if recommendations else None


def main():
    name = input("Name: ").strip()
    print(f"Hello, {name}!\n")

    genres = sorted(set([g.strip() for sublist in movies_df['Genre'].dropna().str.split(',') for g in sublist]))
    print("Genres:", ", ".join(genres))

    while True:
        genre = input ("\n GENRE (NAME OR NUMBER):").strip()
        if genre is digit():
            genre_index = int(genre)
            if 0 <= genre_index < len(genres):
                genre = genres[genre_index]
            else:
                print("Invalid genre number. Please try again.")
                continue
        elif genre.lower() not in (g_lower() for g in genres):
            print("Invalid genre name. Please try again.")
            continue
        
        mood = input("YOUR MOOD: ").strip()
        print("\n analysing mood...")
        poalrity = TextBlob(mood).sentiment.polarity
        print(f"Detected mood polarity: {poalrity:.2f}")

        while True:
            rating_input = input =("MINIMUM RATING (0-10) or `skip' ").strip().lower()
            if rating_input == 'skip':
                rating = None
                break
            try:
                rating = float(rating_input)
                if 0 <= rating <= 10:
                    break
                else:
                    print("Rating must be between 0 and 10. Please try again.")
                
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 10 or 'skip'.")
        print("\n fetching recommendations...")
        recommendations = recommend_movies_debug(genre=genre, mood=mood, rating=rating)
        if recommendations:
            print(f"\n Top {len(recommendations)} movie recommendations for you:")
            for title, polarity in recommendations:
                print(f"- {title} (Polarity: {polarity:.2f})")
        else:
            print("No recommendations found based on your criteria. Please try different inputs.")
        again = input("\nWould you like another recommendation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using Movie Recommender! Goodbye!")
            break
if __name__ == "__main__":
    main()        