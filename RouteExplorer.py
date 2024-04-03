import heapq
def display_menu():
    print("---Location selection menu---")
    print("1 อ.เมืองปราจีนบุรี")
    print("2 Esc bast camp")
    print("3 นํ้าตกเขาอีโต้")
    print("4 รีสอร์ท สจ.บูลย์")
    print("5 อ.ประจันตคาม")
    print("6 แก่งวังไฮ Bytoy")
    print("7 อ.นาดี")
    print("8 สวนลุงบิน")
    print("9 จิบกาเเฟ เเลเขา")
    print("10 ผางามเเคมป์ปิ้ง")
    print("11 เเคมป์ปิ้งวิว วังน้ำเขียว")
    print("12 อ.ศรีมหาโพธิ")
    print("13 ภูริทัศน์รีสอร์ทเเก่งหินเพิง")
    print("14 อ.บ้านสร้าง")
    print("15 บ้านริมน้ำ ณ บางเเตน")
    print("16 ออกจากโปรแกรม")
    
def get_source_and_destination():
    display_menu()
    start_point = input("Select source location (1-15): ")
    end_point = input("Select destination location (1-15): ")

    places = {"1": "อ.เมืองปราจีนบุรี", "2": "Esc bast camp", "3": "นํ้าตกเขาอีโต้", "4": "รีสอร์ท สจ.บูลย์","5": "อ.ประจันตคาม", "6": "แก่งวังไฮ Bytoy", "7": 
        "อ.นาดี", "8": "สวนลุงบิน", "9": "จิบกาเเฟ เเลเขา","10": "ผางามเเคมป์ปิ้ง", "11":  "เเคมป์ปิ้งวิว วังน้ำเขียว", "12":
            "อ.ศรีมหาโพธิ","13": "ภูริทัศน์รีสอร์ทเเก่งหินเพิง", "14": "อ.บ้านสร้าง", "15":  "บ้านริมน้ำ ณ บางเเตน"}
    start = places.get(start_point)
    end = places.get(end_point)

    if start is None or end is None:
        print("Invalid location selection")
        return None, None

    return start, end

import heapq

def find_shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  
    queue = [(0, start)]
    previous_nodes = {}
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    path = []
    current = end
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    path.insert(0, start)
    return path, distances[end]

def main():
    while True:
        start, end = get_source_and_destination()
        if start is None or end is None:
            break

        routes = {
            "อ.เมืองปราจีนบุรี": {"Esc bast camp":19, "นํ้าตกเขาอีโต้":15, "รีสอร์ท สจ.บูลย์":18, "อ.ประจันตคาม":34,"อ.นาดี":68,"อ.ศรีมหาโพธิ":20.5},
            "Esc bast camp": {"อ.เมืองปราจีนบุรี":19, "นํ้าตกเขาอีโต้":8, "รีสอร์ท สจ.บูลย์":9},
            "นํ้าตกเขาอีโต้": {"อ.เมืองปราจีนบุรี":15, "Esc bast camp":8, "รีสอร์ท สจ.บูลย์":12},
            "รีสอร์ท สจ.บูลย์": {"อ.เมืองปราจีนบุรี":18, "Esc bast camp":9, "นํ้าตกเขาอีโต้":12, "อ.ประจันตคาม":37},
            "อ.ประจันตคาม": {"อ.เมืองปราจีนบุรี":34, "แก่งวังไฮ Bytoy":11,"อ.ศรีมหาโพธิ":45},
            "แก่งวังไฮ Bytoy": {"อ.ประจันตคาม":11, "นํ้าตกเขาอีโต้":22},
            "อ.นาดี": {"อ.ประจันตคาม":74,"สวนลุงบิน":35, "จิบกาเเฟ เเลเขา":35,"ผางามเเคมป์ปิ้ง":35,"เเคมป์ปิ้งวิว วังน้ำเขียว":44},
            "สวนลุงบิน": {"จิบกาเเฟ เเลเขา":0.55,"ผางามเเคมป์ปิ้ง":0.45,"เเคมป์ปิ้งวิว วังน้ำเขียว":10,"อ.นาดี":35},
            "จิบกาเเฟ เเลเขา": {"สวนลุงบิน":0.55,"ผางามเเคมป์ปิ้ง":0.9,"เเคมป์ปิ้งวิว วังน้ำเขียว":10.3,"อ.นาดี":35},
            "ผางามเเคมป์ปิ้ง": {"สวนลุงบิน":0.45, "จิบกาเเฟ เเลเขา":0.9,"อ.นาดี":35},
            "เเคมป์ปิ้งวิว วังน้ำเขียว": {"สวนลุงบิน":10, "จิบกาเเฟ เเลเขา":10.3,"ผางามเเคมป์ปิ้ง":6.2,"อ.นาดี":44}, 
            "อ.ศรีมหาโพธิ": {"ภูริทัศน์รีสอร์ทเเก่งหินเพิง":46.1, "อ.ประจันตคาม":33.5,"อ.นาดี":60,"อ.บ้านสร้าง":43.9,"อ.เมืองปราจีนบุรี":20.5},
            "ภูริทัศน์รีสอร์ทเเก่งหินเพิง": {"อ.ศรีมหาโพธิ":11.7,"อ.บ้านสร้าง":84},
             "อ.บ้านสร้าง": {"บ้านริมน้ำ ณ บางเเตน":13, "อ.ประจันตคาม":33.5,"อ.นาดี":60,"อ.ศรีมหาโพธิ":43.9,"อ.เมืองปราจีนบุรี":32},
            "บ้านริมน้ำ ณ บางเเตน": { "อ.บ้านสร้าง":13}
        }


        path, distance = find_shortest_path(routes, start, end)
        print(f"The recommended route from {start} to {end} is: {' -> '.join(path)}, Distance: {distance} km")
        
        
        
if __name__ == "__main__":
    main()
 
