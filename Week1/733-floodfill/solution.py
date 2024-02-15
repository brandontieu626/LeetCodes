class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        rows=len(image)
        cols=len(image[0])

        def flood(r,c,image,oc,color):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=oc:
                return

            image[r][c]=color

            flood(r+1,c,image,oc,color)
            flood(r-1,c,image,oc,color)
            flood(r,c+1,image,oc,color)
            flood(r,c-1,image,oc,color)
        

        flood(sr,sc,image,image[sr][sc],color)

        return image
