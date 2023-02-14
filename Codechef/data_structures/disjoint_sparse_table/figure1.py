from manim import *

class DisjointSparseTableStructure(Scene):
    def create_note(self, txt, scl=0.6):
        text = MathTex(txt).scale(scl)
        box = SurroundingRectangle(text, color=WHITE, buff=0.15)
        return VGroup(box, text)

    def construct(self):
        root = self.create_note(r"A[0, n)").move_to([-1, 3.5, 0])

        node11 = self.create_note(r"A[0, \frac{n}{2})").move_to([-3.5, 2, 0])
        node12 = self.create_note(r"A[\frac{n}{2}, n)").move_to([1.5, 2, 0])

        node21 = self.create_note(r"A[0, \frac{n}{4})").move_to([-4.75, 0, 0])
        node22 = self.create_note(r"A[\frac{n}{4}, \frac{n}{2})").move_to([-2.25, 0, 0])
        node23 = self.create_note(r"A[\frac{n}{2}, \frac{3n}{4})").move_to([0.25, 0, 0])
        node24 = self.create_note(r"A[\frac{3n}{4}, n)").move_to([2.75, 0, 0])

        node31 = self.create_note(r"A[0, 1)").move_to([-6, -3, 0])
        node32 = self.create_note(r"A[1, 2)").move_to([-4.5, -3, 0])
        node33 = self.create_note(r"A[2, 3)").move_to([-3, -3, 0])
        node34 = self.create_note(r"A[n-3, n-2)", 0.5).move_to([0, -3, 0])
        node35 = self.create_note(r"A[n-2, n-1)", 0.5).move_to([2.1, -3, 0])
        node36 = self.create_note(r"A[n-1, n)", 0.5).move_to([4, -3, 0])

        text_height_0 = Tex(r"Depth = 0").scale(0.6).move_to([6, 3.5, 0])
        text_height_1 = Tex(r"Depth = 1").scale(0.6).move_to([6, 2, 0])
        text_height_2 = Tex(r"Depth = 2").scale(0.6).move_to([6, 0, 0])
        text_height_log_n = Tex(r"Depth = log(n)").scale(0.6).move_to([6, -3, 0])

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.add(root)
        self.add(node11)
        self.add(node12)
        self.add(node21)
        self.add(node22)
        self.add(node23)
        self.add(node24)
        self.add(node31)
        self.add(node32)
        self.add(node33)
        self.add(node34)
        self.add(node35)
        self.add(node36)
        self.add(text_height_0)
        self.add(text_height_1)
        self.add(text_height_2)
        self.add(text_height_log_n)
        self.add(Dot(point=[-2.1, -3, 0]))
        self.add(Dot(point=[-1.7, -3, 0]))
        self.add(Dot(point=[-1.3, -3, 0]))
        self.add(Dot(point=[-1, -1, 0]))
        self.add(Dot(point=[-1, -1.5, 0]))
        self.add(Dot(point=[-1, -2, 0]))
        self.add(Line(root.get_bottom(), node11.get_top()))
        self.add(Line(root.get_bottom(), node12.get_top()))
        self.add(Line(node11.get_bottom(), node21.get_top()))
        self.add(Line(node11.get_bottom(), node22.get_top()))
        self.add(Line(node12.get_bottom(), node23.get_top()))
        self.add(Line(node12.get_bottom(), node24.get_top()))

        self.add(Line(node21.get_bottom(), [node21.get_bottom()[0]-0.5, node21.get_bottom()[1]-0.5, node21.get_bottom()[2]]))
        self.add(Line(node21.get_bottom(), [node21.get_bottom()[0]+0.5, node21.get_bottom()[1]-0.5, node21.get_bottom()[2]]))
        self.add(Line(node22.get_bottom(), [node22.get_bottom()[0]-0.5, node22.get_bottom()[1]-0.5, node22.get_bottom()[2]]))
        self.add(Line(node22.get_bottom(), [node22.get_bottom()[0]+0.5, node22.get_bottom()[1]-0.5, node22.get_bottom()[2]]))
        self.add(Line(node23.get_bottom(), [node23.get_bottom()[0]-0.5, node23.get_bottom()[1]-0.5, node23.get_bottom()[2]]))
        self.add(Line(node23.get_bottom(), [node23.get_bottom()[0]+0.5, node23.get_bottom()[1]-0.5, node23.get_bottom()[2]]))
        self.add(Line(node24.get_bottom(), [node24.get_bottom()[0]-0.5, node24.get_bottom()[1]-0.5, node24.get_bottom()[2]]))
        self.add(Line(node24.get_bottom(), [node24.get_bottom()[0]+0.5, node24.get_bottom()[1]-0.5, node24.get_bottom()[2]]))

        self.add(Line(node31.get_top(), [node31.get_top()[0]+0.5, node31.get_top()[1]+0.5, node31.get_top()[2]]))
        self.add(Line(node32.get_top(), [node32.get_top()[0]-0.5, node32.get_top()[1]+0.5, node32.get_top()[2]]))
        self.add(Line(node33.get_top(), [node33.get_top()[0]+0.5, node33.get_top()[1]+0.5, node33.get_top()[2]]))
        self.add(Line(node34.get_top(), [node34.get_top()[0]-0.5, node34.get_top()[1]+0.5, node34.get_top()[2]]))
        self.add(Line(node35.get_top(), [node35.get_top()[0]+0.5, node35.get_top()[1]+0.5, node35.get_top()[2]]))
        self.add(Line(node36.get_top(), [node36.get_top()[0]-0.5, node36.get_top()[1]+0.5, node36.get_top()[2]]))
