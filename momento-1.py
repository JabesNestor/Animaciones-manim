import manium

class EsperanzaConRecuadros(Scene):
    def construct(self):
        
        descripcion = Text(
            "Primer momento = Media aritmética",
            font_size=30
        ).to_edge(UP, buff=0.8)

       
        notacion = MathTex(r"\mu = E[X]", font_size=50).next_to(descripcion, DOWN, buff=0.8)

        disc_formula = MathTex(
            r"E[X] = \sum_{i} x_i \cdot P(X = x_i)",
            font_size=32
        )
        disc_box = SurroundingRectangle(disc_formula, color=BLUE, buff=0.2)
        disc_label = Text("Discreto", font_size=24, color=BLUE).next_to(disc_box, UP, buff=0.1)
        grupo_disc = VGroup(disc_label, disc_box, disc_formula)

        
        cont_formula = MathTex(
            r"E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x) \, dx",
            font_size=32
        )
        cont_box = SurroundingRectangle(cont_formula, color=GREEN, buff=0.2)
        cont_label = Text("Continuo", font_size=24, color=GREEN).next_to(cont_box, UP, buff=0.1)
        grupo_cont = VGroup(cont_label, cont_box, cont_formula)

    
        grupos = VGroup(grupo_disc, grupo_cont).arrange(RIGHT, buff=1).next_to(notacion, DOWN, buff=1)

        # Animaciones
        self.play(FadeIn(descripcion))
        self.wait(0.5)
        self.play(Write(notacion))
        self.wait(1)
        self.play(
            Create(disc_box),
            Write(disc_formula),
            Write(disc_label)
        )
        self.wait(1)
        self.play(
            Create(cont_box),
            Write(cont_formula),
            Write(cont_label)
        )
        self.wait(30)

%manim -qm -v WARNING EsperanzaConRecuadros