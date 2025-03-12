class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def generate_row ( row):
            if row == 0:
                return [1]
            if row == 1:
                return [1,1]
      
            previous_row = generate_row(row - 1)
            current_row = [1]
            for idx in range(len(previous_row)-1):
                current_row.append(previous_row[idx] + previous_row[idx+1])
            current_row.append(1)
            return current_row
        return generate_row(rowIndex)
            