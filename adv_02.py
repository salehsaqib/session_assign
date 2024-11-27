def main():            
    earthWt = float(input("Enter weight on Earth : "))
    planetName = str(input("Enter Planet Name : "))
    planetName = planetName.lower()
    match planetName:
        case 'mercury':
            wtFactor=float(37.6)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case 'venus':
            wtFactor=float(88.9)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case 'mars':
            wtFactor=float(37.8)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case 'jupiter':
            wtFactor=float(236.0)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case 'saturn':
            wtFactor=float(108.1)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case 'uranus':
            wtFactor=float(81.5)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case 'neptune':
            wtFactor=float(114.0)
            planetName = planetName.capitalize()
            print(f"The equivalent weight on {planetName} is {round((earthWt*wtFactor/100),2)}")
        case _:
            print(f"The Planet {planetName} is not discovered Yet :-)")
        

    
    
        
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()