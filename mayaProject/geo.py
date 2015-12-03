import requests

#this builds our FIPS query and extracts the interesting bits from it
def getFIPS(lat, lon, lev):
    queryString = "http://data.fcc.gov/api/block/find?latitude=" + str(lat)
    queryString += "&longitude=" + str(lon) + "&showall=false&format=json"

    fResponse = requests.get(queryString)

    FIPS = fResponse.json()[lev]['FIPS']
    return FIPS

def getInfo(lat, lon):
    
    # first we set our API key. This will expire before too long, but
    # getting another one is easy.
    key = "993fe969db5b1d642b17df8cc66f26ad98f9009e"
    # then we get our FIPS variable to index into our location.
    fps = getFIPS(lat, lon, 'Block') # leave this as block until we figure out why not to.
    dataCode = "B00001_001E" # B00001_001E
    stateCode = fps[:2]
    countyCode = fps[2:5]
    tractCode = fps[5:11]
    blockCode = fps[11:]
    queryString  = "http://api.census.gov/data/2013/acs5?get=" + dataCode
    queryString += "&for=tract:" + tractCode + "&in=state: " + stateCode
    queryString += "+county:" + countyCode + "&key=" + key
    req = requests.get(queryString)
    if req.status is 200:
        req = req.json()
    else:
        return req.status
    return req

# <var xml:id="DP03_0094E" label="INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Median earnings for female full-time, year-round workers (dollars)" concept="SELECTED ECONOMIC CHARACTERISTICS" predicate-type="int"/>
# <var xml:id="DP03_0094M" label="INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Median earnings for female full-time, year-round workers (dollars)" concept="SELECTED ECONOMIC CHARACTERISTICS" predicate-type="int"/>
# <var xml:id="DP03_0093M" label="INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Median earnings for male full-time, year-round workers (dollars)" concept="SELECTED ECONOMIC CHARACTERISTICS" predicate-type="int"/>
# <var xml:id="DP03_0093E" label="INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Median earnings for male full-time, year-round workers (dollars)" concept="SELECTED ECONOMIC CHARACTERISTICS" predicate-type="int"/>

# <var xml:id="DP03_0092M" label="INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Median earnings for workers (dollars)" concept="SELECTED ECONOMIC CHARACTERISTICS" predicate-type="int"/>
# <var xml:id="DP03_0092E" label="INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS)!!Median earnings for workers (dollars)" concept="SELECTED ECONOMIC CHARACTERISTICS" predicate-type="int"/>
