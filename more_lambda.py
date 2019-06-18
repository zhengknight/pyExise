#lambda表达式演示（lambda expression有时也称lambda forms）
points = [{'x':3,'y':4},{'x':2, 'y':1}]

points.sort(key=lambda i:i['y'])

print(points)