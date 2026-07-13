import altair as alt

data={'day': 1,
      
      'Price':45}
data2={
    'day': 1 , 'Price':69 
}
chart=alt.Chart(alt.Data(values=data)).mark_line().encode()
x= 'Day:H'
y= 'Price:H'
