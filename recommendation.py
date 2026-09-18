import argparse
from .analytics import dataset_summary, feature_importance
from .model import train_model
from .predictor import predict_risk
from .recommendation import recommendations
from .reporting import print_metrics

def sample_record():
    return {
        "attendance": 72,
        "study_hours": 3.5,
        "assignment_completion": 68,
        "internal_marks": 55,
        "previous_gpa": 6.2,
        "sleep_hours": 5.5,
        "backlogs": 1,
    }

def run_sample_prediction():
    record = sample_record()
    result = predict_risk(record)
    print("Sample Prediction")
    print("-----------------")
    print("Risk Level:", result["risk_level"])
    print("Confidence:", result["confidence"])
    print("\nRecommendations:")
    for item in recommendations(record, result["risk_level"]):
        print("-", item)

def run_demo():
    from .generate_dataset import generate_dataset
    generate_dataset()
    train_model()
    print("\nDataset Summary")
    print("----------------")
    print(dataset_summary())
    print("\nFeature Importance")
    print("------------------")
    for feature, importance in feature_importance().items():
        print(f"{feature}: {importance:.4f}")
    print()
    run_sample_prediction()
    print()
    print_metrics()

def interactive_menu():
    while True:
        print("\n=== EduPredict: Student Academic Risk Analyzer ===")
        print("1. Train model")
        print("2. Run sample prediction")
        print("3. Analyze dataset")
        print("4. Show metrics")
        print("5. Run complete demo")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                train_model()
            elif choice == "2":
                run_sample_prediction()
            elif choice == "3":
                print(dataset_summary())
                print(feature_importance())
            elif choice == "4":
                print_metrics()
            elif choice == "5":
                run_demo()
            elif choice == "6":
                print("Exiting EduPredict.")
                break
            else:
                print("Invalid choice. Enter 1 to 6.")
        except Exception as error:
            print("Error:", error)

def main():
    parser = argparse.ArgumentParser(description="EduPredict command-line academic risk analyzer")
    parser.add_argument(
        "command", nargs="?",
        choices=["generate", "train", "predict", "analyze", "metrics", "demo", "interactive"],
        default="interactive"
    )
    args = parser.parse_args()

    if args.command == "generate":
        from .generate_dataset import generate_dataset
        generate_dataset()
    elif args.command == "train":
        train_model()
    elif args.command == "predict":
        run_sample_prediction()
    elif args.command == "analyze":
        print("Dataset Summary")
        print(dataset_summary())
        print("\nFeature Importance")
        for feature, importance in feature_importance().items():
            print(f"{feature}: {importance:.4f}")
    elif args.command == "metrics":
        print_metrics()
    elif args.command == "demo":
        run_demo()
    else:
        interactive_menu()

if __name__ == "__main__":
    main()
