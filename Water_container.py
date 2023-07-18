   def maxArea(height):
        max_area = 0
        left_index = 0
        right_index = len(height)-1

        while left_index < right_index:
            width = right_index - left_index
            low_height = min(height[left_index], height[right_index])
            area = width * low_height 
            #print(width,low_height,area)
            if area > max_area:
                max_area = area

            if height[left_index] <= height[right_index]:  
                left_index += 1
            else:
                right_index -= 1
        return max_area     