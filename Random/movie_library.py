# create movie library
# must be able to add new movies to the library
# must be able to view all movies in collection
# must be able to find a particular movie by any of its attributes.

movie_collection = []

USER_PROMPT = 'Hi. Enter "a" to add a movie, "f" \n to find a movie, "w" to see \n the movie or "q" to quit the app. Enter your selection: '


def watch_movie(movie_name):
  if movie_name != None:
    movie_to_play = find_movie(movie_name)
    if movie_to_play != None:
      print(f'Your movie: {movie_to_play} will start momentarily')
  else:
    print('Please enter valid movie name.')

def add_movie(movie_name, movie_director, year):
  for movie in movie_collection:
    if movie['name'] == movie_name and movie['director'] == movie_director:
      print(f'{movie_director}\'s {movie_name} is already in the collection.')
  else:
    new_entry = {
      'name': movie_name,
      'director': movie_director,
      'year': int(year)
    }
    movie_collection.append(new_entry)
    print(f'{movie_director}\'s {movie_name} has been added to your collection')
  return movie_collection


def list_movies():
  for movie in movie_collection:
    print(movie['name'])


def find_movie(movie_name):
  for movie in movie_collection:
    if movie['name'] == movie_name:
      print(f'{movie_name} is in your collection!')
      return movie['name']
  else:
    print(f'Sorry, but {movie_name} is not in your collection.')


def main():
  selection = input(USER_PROMPT)
  while selection != 'q':
    if selection == 'a':
      movie_name = input('What\'s the name of the movie you\'d like to add?: ')
      movie_director = input(f'Please tell me the name of the director for {movie_name}: ')
      year = int(input(f'What was the release year for {movie_name}?: '))
      add_movie(movie_name, movie_director, year)
    elif selection == 'f':
      movie_name = input('Tell me the name of the movie you are looking for: ')
      find_movie(movie_name)
    elif selection == 'w':
      movie_name = input('What movie would you like to watch?: ')
      watch_movie(movie_name)
    else:
      print('Sorry, you\'ve entered an incorrect command. Try again.')
    selection = input(USER_PROMPT)


main()
