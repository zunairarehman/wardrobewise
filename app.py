from flask import Flask , render_template ,request # type: ignore
app = Flask(__name__)

@app.route("/")
def default():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():        
    return render_template("about.html")

@app.route("/review")
def member():
    return render_template("review.html")


@app.route("/select")
def select():
    return render_template("selection.html")


@app.route('/suggest', methods=['POST'])
def suggest():
    # Retrieve user input from the form
    gender = request.form.get('gender')
    occasion = request.form.get('occasion')

    # Log the values to the console
    print(f"Gender: {gender}, Occasion: {occasion}")
    # Outfit suggestions with unique links for each combination

    if gender == 'F' and occasion == 'CO':
        outfits = [
           "CF1.jpeg",
           "CF2.jpeg",
           "CF3.jpeg",
           "CF4.jpeg",
           "CF5.jpeg",
           "CF6.jpeg",
           "CF7.jpeg",
           "CF8.jpeg",
           "CF9.jpeg",
           "CF10.jpeg",
           "CF11.jpeg",
           "CF12.jpeg",
           "CF13.jpeg",
           "CF14.jpeg",
           "CF15.jpeg",
           "CF16.jpeg",
           "CF17.jpeg",
           "CF18.jpeg",
           "CF19.jpeg",
           "CF20.jpeg",
           "CF21.jpeg",
           "CF22.jpeg",
           "CF23.jpeg",
           "CF24.jpeg",
           "CF25.jpeg",
           "CF26.jpeg",
           "CF27.jpeg",
           "CF28.jpeg",
           "CF29.jpeg",
           "CF30.jpg"
        ]
    elif gender == 'M' and occasion == 'CO':
        outfits = [
            "CM1.jpeg",
            "CM2.jpeg",
            "CM3.jpeg",
            "CM4.jpeg",
            "CM5.jpeg",
            "CM6.jpeg",
            "CM7.jpeg",
            "CM8.jpeg",
            "CM9.jpeg",
            "CM10.jpeg",
            "CM11.jpeg",
            "CM12.jpeg",
            "CM13.jpeg",
            "CM14.jpeg",
            "CM15.jpeg",
            "CM16.jpeg",
            "CM17.jpg",
            "CM18.jpeg",
            "CM19.jpeg",
            "CM20.jpeg",
            "CM21.jpeg",
            "CM22.jpeg",
            "CM23.jpeg",
            "CM24.jpeg",
            "CM25.jpeg",
            "CM26.jpeg",
            "CM27.jpeg",
            "CM28.jpeg",
            "CM29.jpeg",
            "CM30.jpeg"
        ]
    elif (gender == 'F' or gender == 'M') and occasion == 'CPO':
        outfits = [
            "cpw1.jpg",
            "cpw2.jpg",
            "cpw3.jpg",
            "cpw4.jpg",
            "cpw5.jpg",
            "cpw6.jpg",
            "cpw7.jpg",
            "cpw8.jpg",
            "cpw9.jpg",
            "cpw10.jpg",
            "cpw11.jpg",
            "cpw12.jpg",
            "cpw13.jpg",
            "cpw14.jpg",
            "cpw15.jpg",
            "cpw16.jpg",
            "cpw17.jpg",
            "cpw18.jpg",
            "cpw19.jpg",
            "cpw20.jpg",
            "cpw21.jpg"
        ]
    elif gender == 'F' and occasion == 'FC':
        outfits = [
           "FF.jpeg",
           "FF1.jpeg",
           "FF2.jpeg",
           "FF3.jpeg",
           "FF4.jpeg",
           "FF5.jpeg",
           "FF6.jpeg",
           "FF7.jpeg",
           "FF8.jpeg",
           "FF9.jpeg",
           "FF10.jpeg",
           "FF11.jpeg",
           "FF12.jpeg",
           "FF13.jpeg",
           "FF14.jpeg",
           "FF15.jpeg",
           "FF16.jpeg",
           "FF17.jpeg",
           "FF18.jpeg",
           "FF19.jpeg",
           "FF20.jpeg",
           "FF21.jpeg",
           "FF22.jpeg",
           "FF23.jpeg",
           "FF24.jpeg",
           "FF25.jpeg",
           "FF26.jpeg",
           "FF27.jpeg",
           "FF28.jpeg",
           "FF29.jpeg",
           "FF30.jpeg"
        ]
    elif gender == 'M' and occasion == 'FC':
        outfits = [
           "MFES1.jpeg",
           "MFES2.jpeg",
           "MFES3.jpeg",
           "MFES4.jpeg",
           "MFES5.jpeg",
           "MFES6.jpeg",
           "MFES7.jpeg",
           "MFES8.jpeg",
           "MFES9.jpeg",
           "MFES10.jpeg",
           "MFES11.jpeg",
           "MFES12.jpeg",
           "MFES13.jpeg",
           "MFES14.jpeg",
           "MFES15.jpeg",
           "MFES16.jpeg",
           "MFES17.jpeg",
           "MFES18.jpeg",
           "MFES19.jpeg",
           "MFES20.jpeg",
           "MFES21.jpeg",
           "MFES22.jpeg",
           "MFES23.jpeg",
           "MFES24.jpeg",
           "MFES25.jpeg",
           "MFES26.jpeg",
           "MFES27.jpeg",
           "MFES28.jpeg",
           "MFES29.jpeg",
           "MFES30.jpeg"
        ]
    elif gender == 'F' and occasion == 'BM':
        outfits = [
            "MF01.jpg",
            "MF02.jpg",
            "MF03.jpg",
            "MF04.jpg",
            "MF05.jpg",
            "MF06.jpg",
            "MF07.jpg",
            "MF08.jpg",
            "MF09.jpg",
            "MF10.jpg",
            "MF11.jpg",
            "MF12.jpg",
            "MF13.jpg",
            "MF14.jpg",
            "MF15.jpg",
            "MF16.jpg",
            "MF17.jpg",
            "MF18.jpg",
            "MF19.jpg",
            "MF20.jpg"
        ]
    elif gender == 'M' and occasion == 'BM':
        outfits = [
            "MM1.jpg",
            "MM2.jpg",
            "MM3.jpg",
            "MM4.jpg",
            "MM5.jpg",
            "MM6.jpg",
            "MM7.jpg",
            "MM8.jpg",
            "MM9.jpg",
            "MM10.jpg",
            "MM11.jpg",
            "MM12.jpg",
            "MM13.jpg",
            "MM14.jpg",
            "MM15.jpg",
            "MM16.jpg",
            "MM17.jpg",
            "MM18.jpg",
            "MM19.jpg",
            "MM20.jpg"
        ]

    elif gender == 'M' and occasion == 'WBG':
        outfits = [
            "WG1.jpg",
            "WG2.jpg",
            "WG3.jpg",
            "WG4.jpg",
            "WG5.jpg",
            "WG6.jpg",
            "WG7.jpg",
            "WG8.jpg",
            "WG9.jpg",
            "WG10.jpg",
            "WG11.jpg",
            "WG12.jpg",
            "WG13.jpg",
            "WG14.jpg",
            "WG15.jpg",
            "WG16.jpg",
            "WG17.jpg",
            "WG18.jpg",
            "WG19.jpg",
            "WG20.jpg",
            "WG21.jpg",
            "WG22.jpg",
            "WG23.jpg",
            "WG24.jpg",
            "WG25.jpg",
        ]
    elif gender == 'F' and occasion == 'WBG':
        outfits = [
          "WB1.jpg",
          "WB2.jpg",
          "WB3.jpg",
          "WB4.jpg",
          "WB5.jpg",
          "WB6.jpg",
          "WB7.jpg",
          "WB8.jpg",
          "WB9.jpg",
          "WB10.jpg",
          "WB11.jpg",
          "WB12.jpg",
          "WB13.jpg",
          "WB14.jpg",
          "WB15.jpg",
          "WB16.jpg",
          "WB17.jpg",
          "WB18.jpg",
          "WB19.jpg",
          "WB20.jpg",
          "WB21.jpg",
          "WB22.jpg",
          "WB23.jpg",
          "WB24.jpg",
        ]
    elif gender == 'F' and occasion == 'WG':
        outfits = [
            "WGF1.jpg",
            "WGF2.jpg",
            "WGF3.jpg",
            "WGF4.jpg",
            "WGF5.jpg",
            "WGF6.jpg",
            "WGF7.jpg",
            "WGF8.jpg",
            "WGF9.jpg",
            "WGF10.jpg",
            "WGF11.jpg",
            "WGF12.jpg",
            "WGF13.jpg",
            "WGF14.jpg",
            "WGF15.jpg",
            "WGF16.jpg",
            "WGF17.jpg",
            "WGF18.jpg",
            "WGF19.jpg",
            "WGF20.jpg",
            "WGF21.jpg",
            "WGF22.jpg",
            "WGF23.jpg",
            "WGF24.jpg",
            "WGF25.jpg",
            "WGF26.jpg",
            "WGF27.jpg",
            "WGF28.jpg",
            "WGF29.jpg",
            "WGF30.jpg"
        ]
    elif gender == 'M' and occasion == 'WG':
        outfits = [
            "WGM1.jpg",
            "WGM2.jpg",
            "WGM3.jpg",
            "WGM4.jpg",
            "WGM5.jpg",
            "WGM6.jpg",
            "WGM7.jpg",
            "WGM8.jpg",
            "WGM9.jpg",
            "WGM10.jpg",
            "WGM11.jpg",
            "WGM12.jpg",
            "WGM13.jpg",
            "WGM14.jpg",
            "WGM15.jpg",
            "WGM16.jpg",
            "WGM17.jpg",
            "WGM18.jpg",
            "WGM19.jpg",
            "WGM20.jpg",
            "WGM21.jpg",
            "WGM22.jpg",
            "WGM23.jpg",
            "WGM24.jpg",
            "WGM25.jpg"
        ]
    
    else:
        return "No outfit found for the selected options. Please try again."

    return render_template('suggestion.html', outfits=outfits)


if __name__ == '__main__':
    app.run(debug=True)