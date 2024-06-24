class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        resulting_image = []
        for i in image:
            i.reverse()
            resulting_image.append([x^1 for x in i])
        return resulting_image