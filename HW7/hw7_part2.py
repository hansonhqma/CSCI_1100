'''

Author - Hanson Ma

hanson.hq.ma@gmail.com

https://www.github.com/hansonhqma

'''
import json



def buildlibrary(yearmin, yearmax, genre, moviedict, ratingdict, w1, w2): #build library function, creates two dictionaries used in indexing later
    out = dict()
    ratings = dict()
    keylist = list(moviedict.keys())
    genre = genre.lower()
    for key in keylist: #for each dictionary item
        subjectmovie = moviedict[key]
        year = subjectmovie['movie_year']
        genrelist = []
        for i in range(len(subjectmovie['genre'])):
            genrelist.append(subjectmovie['genre'][i].lower())
        ratestatus = key in list(ratingdict.keys()) and len(ratingdict[key]) >= 3 #check if twitter rating is valid
        if year >= yearmin and year <= yearmax and genre in genrelist and ratestatus:
            rating = (w1 * subjectmovie['rating'] + w2 * (sum(ratingdict[key]) / len(ratingdict[key]))) / (w1 + w2)
            out[key] = subjectmovie
            ratings[rating] = key #rating as key for ease of indexing later

    return out, ratings

if __name__ == "__main__": #main function
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    minyear = input("Min year => ")
    print(minyear)
    maxyear = input("Max year => ")
    print(maxyear)
    imdbweight = input("Weight for IMDB => ")
    print(imdbweight)
    twitterweight = input("Weight for Twitter => ")
    print(twitterweight)

    while True:
        genre = input("\nWhat genre do you want to see? ")
        print(genre)
        if genre.lower() == "stop":
            break

        moviedict, ratingdict = buildlibrary(int(minyear), int(maxyear), genre, movies, ratings, float(imdbweight), float(twitterweight))
        if len(moviedict) == 0 and len(ratingdict) == 0: #if genre not found
            print("\nNo {} movie found in {} through {}".format(genre.title(), minyear, maxyear))
            continue

        maxrate, minrate = max(list(ratingdict.keys())), min(list(ratingdict.keys())) #find max and min ratings
        maxkey, minkey = ratingdict[maxrate], ratingdict[minrate] #find respective keys based on max and min ratings

        print("\nBest:\n\tReleased in {}, {} has a rating of {:.2f}\n".format(moviedict[maxkey]["movie_year"], moviedict[maxkey]["name"], maxrate)) #print statements
        print("Worst:\n\tReleased in {}, {} has a rating of {:.2f}".format(moviedict[minkey]["movie_year"], moviedict[minkey]["name"], minrate))