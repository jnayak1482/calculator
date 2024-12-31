import streamlit as st
import pandas as pd

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Professional Calculator",
        page_icon="🧮",
        layout="centered"
    )

    # Custom CSS to improve the appearance
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            margin-bottom: 10px;
        }
        .result-text {
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
            border-radius: 5px;
            background-color: #f0f2f6;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("Professional Calculator")
    st.markdown("---")

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    # Input fields
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, step=0.1)

    # Operation selection
    operation = st.selectbox(
        "Select Operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    # Calculate button
    if st.button("Calculate", key="calc_button"):
        try:
            if operation == "Addition":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication":
                result = num1 * num2
                symbol = "×"
            else:  # Division
                if num2 == 0:
                    st.error("Error: Division by zero is not allowed!")
                    return
                result = num1 / num2
                symbol = "÷"

            # Display the result with equation
            st.markdown(f"""
                <div class='result-text'>
                    {num1} {symbol} {num2} = {result:.2f}
                </div>
            """, unsafe_allow_html=True)

            # Create a history dataframe
            if 'calculation_history' not in st.session_state:
                st.session_state.calculation_history = pd.DataFrame(
                    columns=['First Number', 'Operation', 'Second Number', 'Result']
                )

            # Add current calculation to history
            new_row = pd.DataFrame({
                'First Number': [num1],
                'Operation': [symbol],
                'Second Number': [num2],
                'Result': [result]
            })
            st.session_state.calculation_history = pd.concat(
                [new_row, st.session_state.calculation_history]
            ).reset_index(drop=True)

            # Display calculation history
            st.markdown("### Calculation History")
            st.dataframe(
                st.session_state.calculation_history,
                use_container_width=True
            )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown("Jinendra Nayak❤️")
    #st.markdown("")

if __name__ == "__main__":
    main()