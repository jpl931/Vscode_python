function calculateDaysBetweenDates(begin, end) {
    var startDay = new Date(begin);
    var endDay = new Date(end);
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var diffDays = Math.round(Math.abs((startDay.getTime() - endDay.getTime())/(oneDay)));
    return diffDays;
}{
    
}