def local_config(SALEBOX):
    SALEBOX['API'] = {
        'IP': 'x.x.x.x',  # Enter your Salebox backoffice IP address here
        'URL': 'https://xxx.salebox.io',  # Enter your Salebox backoffice IP address here
        'KEY': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',  # Enter your Salebox ecommerce key here
        'LICENSE': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',  # Enter your Salebox ecommerce license here
    }
    SALEBOX['MISC']['POS_USER_ID'] = x   # Enter your Salebox POS user ID number here
    return SALEBOX
