#this program prints the search the cities within the list of available cities
def find_city_index(cities, search_city):
    try:
        index = [city.lower() for city in cities].index(search_city.lower())
        return f"'{search_city}' found at index: {index}"
    except ValueError:
        return f"'{search_city}' not found in the list"
    except AttributeError:
        return "Error: City names must be strings"
    except Exception as e:
        return f"An error occurred: {str(e)}"
def test_find_city_index():
    city_list = ["New York", "London", "Paris", "Tokyo", "Sydney"]
    tests = [
        (city_list, "Paris"),    
        (city_list, "paris"),    
        (city_list, "Berlin"),  
        (city_list, 123),        
        ([], "London"),          
        (city_list, "new york"), 
        (["tokyo", "london"], "Tokyo")  
    ]
    
    for cities, city in tests:
        print(f"\nSearching for '{city}' in {cities}:")
        print(find_city_index(cities, city))

if __name__ == "__main__":
    print("CITY SEARCH TESTING")
    test_find_city_index()
