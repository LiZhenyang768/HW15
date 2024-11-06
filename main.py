def errorcode(x):
    match x:
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case 401:
            print("Unauthorised")
        case 403:
            print("Forbidden")
        case 501:
            print("Not Implemented")
        case 502:
            print("Service Temporarily Overloaded")
        case 503:
            print("Service Unavailable")
x=float(input("x :"))
print(errorcode(x))




