Step 1 
    purchase or use Mecha treasure chest from flotilla ('https://shop.pimoroni.com/products/flotilla-mega-treasure-chest')

Step 2 
    plugin your RasPi kit

Step 3
    Unbox your Mecha treasure chest

Step 4 
    make sure you are connected to wifi and run 
    curl -sS get.pimoroni.com/flotilla | bash in your terminal 
    (ArteveldeHS cable network will not let you run the curl command)
    
Step 5
    Plugin the dock (red wire) into your RasPi

Step 6
    create a test file 
     ----------------------------
    |   import flotilla          |
    |   dock = flotilla.Client() |
    |   print(dock)              |
     ----------------------------
Step 7
    run in terminal
        python file.py
    
    if you get a response your dock is connected
