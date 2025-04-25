monthConversions = {
    "Jan": "Janauary",
    "Feb" :"February",
    "Mar" :"March",
    "Apr" :"April",
    "May" :"May",
    "Jun" :"June",
    "Jul" :"July",
    "Aug" :"August",
    "Sep" :"September",
    "Oct" :"October",
    "Nov" :"November",
    "Dec" :"December"

}

print(monthConversions.get("Mar"))
print(monthConversions.get("Mac", "Not a valid key"))