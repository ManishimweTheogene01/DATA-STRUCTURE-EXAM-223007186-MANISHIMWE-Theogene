#include <iostream>
#include <cstring>

using namespace std;

// Task 1: Define the State structure
struct State {
    char color[10];
    int duration;
};

// Abstract base class
class TrafficLightController {
protected:
    State* states;
    int numStates;
    int currentState;

public:
    TrafficLightController(int n) : numStates(n), currentState(0) {
        states = new State[n];
    }

    virtual ~TrafficLightController() {
        delete[] states;
    }

    virtual void cycle() = 0;
};

// Urban Controller
class UrbanController : public TrafficLightController {
public:
    UrbanController() : TrafficLightController(3) {
        strcpy(states[0].color, "Red");
        states[0].duration = 60;
        strcpy(states[1].color, "Green");
        states[1].duration = 45;
        strcpy(states[2].color, "Yellow");
        states[2].duration = 5;
    }

    void cycle() override {
        cout << "[Urban] Color: " << states[currentState].color
             << ", Duration: " << states[currentState].duration << "s\n";
        currentState = (currentState + 1) % numStates;
    }
};

// Pedestrian Controller
class PedestrianController : public TrafficLightController {
public:
    PedestrianController() : TrafficLightController(2) {
        strcpy(states[0].color, "Red");
        states[0].duration = 30;
        strcpy(states[1].color, "Green");
        states[1].duration = 15;
    }

    void cycle() override {
        cout << "[Pedestrian] Color: " << states[currentState].color
             << ", Duration: " << states[currentState].duration << "s\n";
        currentState = (currentState + 1) % numStates;
    }
};

// Custom Controller with user-defined states
class CustomController : public TrafficLightController {
public:
    CustomController(int n) : TrafficLightController(n) {
        for (int i = 0; i < n; ++i) {
            cout << "Enter color for state " << i + 1 << ": ";
            cin >> ws; // clear whitespace
            cin.getline(states[i].color, 10);

            cout << "Enter duration (in seconds) for " << states[i].color << ": ";
            cin >> states[i].duration;
        }
    }

    void cycle() override {
        cout << "[Custom] Color: " << states[currentState].color
             << ", Duration: " << states[currentState].duration << "s\n";
        currentState = (currentState + 1) % numStates;
    }
};

// Global controller list
TrafficLightController** controllers = nullptr;
int controllerCount = 0;

// Add a controller
void addController(TrafficLightController* c) {
    TrafficLightController** temp = new TrafficLightController*[controllerCount + 1];
    for (int i = 0; i < controllerCount; ++i) {
        temp[i] = controllers[i];
    }
    temp[controllerCount++] = c;
    delete[] controllers;
    controllers = temp;
}

// Remove controller by index
void removeController(int index) {
    if (index < 0 || index >= controllerCount) return;

    TrafficLightController** temp = new TrafficLightController*[controllerCount - 1];
    int j = 0;
    for (int i = 0; i < controllerCount; ++i) {
        if (i != index) {
            temp[j++] = controllers[i];
        } else {
            delete controllers[i];
        }
    }
    --controllerCount;
    delete[] controllers;
    controllers = temp;
}

// Simulate a cycle for all controllers
void simulateCycle() {
    for (int i = 0; i < controllerCount; ++i) {
        controllers[i]->cycle();
    }
}

// Main program
int main() {
    int totalControllers;
    cout << "Enter the number of traffic light controllers to add: ";
    cin >> totalControllers;

    for (int i = 0; i < totalControllers; ++i) {
        cout << "\n--- Controller " << i + 1 << " ---\n";
        cout << "Select controller type:\n";
        cout << "1. Urban\n";
        cout << "2. Pedestrian\n";
        cout << "3. Custom (user-defined)\n";
        cout << "Enter choice (1-3): ";
        int type;
        cin >> type;

        if (type == 1) {
            addController(new UrbanController());
        } else if (type == 2) {
            addController(new PedestrianController());
        } else if (type == 3) {
            int n;
            cout << "Enter number of states: ";
            cin >> n;
            addController(new CustomController(n));
        } else {
            cout << "Invalid choice. Skipping this controller.\n";
        }
    }

    int numCycles;
    cout << "\nEnter number of cycles to simulate: ";
    cin >> numCycles;

    for (int i = 0; i < numCycles; ++i) {
        cout << "\n=== Cycle " << i + 1 << " ===\n";
        simulateCycle();
    }

    // Ask if user wants to remove a controller
    char removeOption;
    cout << "\nDo you want to remove any controller? (y/n): ";
    cin >> removeOption;
    if (removeOption == 'y' || removeOption == 'Y') {
        int removeIndex;
        cout << "Enter index of controller to remove (0 to " << controllerCount - 1 << "): ";
        cin >> removeIndex;
        removeController(removeIndex);

        // Show one more cycle after removal
        cout << "\nCycle after removal:\n";
        simulateCycle();
    }

    // Cleanup all controllers
    while (controllerCount > 0) {
        removeController(0);
    }

    cout << "\nAll controllers removed. Program ended.\n";
    return 0;
}
