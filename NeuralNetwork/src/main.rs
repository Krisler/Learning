use ndarray::prelude::*;
use ndarray_rand::RandomExt;
use rand_distr::Normal;

// Activation functions enum
#[derive(Clone, Copy)]
enum Activation {
    ReLU,
    Sigmoid,
}

impl Activation {
    // Apply activation function
    fn apply(&self, z: &Array2<f32>) -> Array2<f32> {
        match self {
            Self::ReLU => z.mapv(|x| x.max(0.0)),
            Self::Sigmoid => z.mapv(|x| 1.0 / (1.0 + (-x).exp())),
        }
    }

    // Calculate activation derivative
    fn derivative(&self, z: &Array2<f32>) -> Array2<f32> {
        match self {
            Self::ReLU => z.mapv(|x| if x > 0.0 { 1.0 } else { 0.0 }),
            Self::Sigmoid => {
                let s = self.apply(z);
                &s * (1.0 - &s)
            }
        }
    }
}

// Neural network layer
struct Layer {
    weights: Array2<f32>,
    biases: Array2<f32>,
    activation: Activation,
}

impl Layer {
    // Initialize layer with proper weight initialization
    fn new(input_size: usize, output_size: usize, activation: Activation) -> Self {
        let std_dev = match activation {
            Activation::ReLU => (2.0 / input_size as f32).sqrt(),
            Activation::Sigmoid => (1.0 / input_size as f32).sqrt(),
        };
        
        let weights = Array2::random(
            (input_size, output_size),
            Normal::new(0.0, std_dev).unwrap(),
        );
        
        let biases = Array2::zeros((1, output_size));

        Self {
            weights,
            biases,
            activation,
        }
    }

    // Forward propagation with cache
    fn forward(&self, input: &Array2<f32>) -> (Array2<f32>, (Array2<f32>, Array2<f32>)) {
        let z = input.dot(&self.weights) + &self.biases;
        let a = self.activation.apply(&z);
        (a, (input.clone(), z))
    }

    // Backward propagation
    fn backward(
        &self,
        d_a: &Array2<f32>,
        cache: &(Array2<f32>, Array2<f32>),
    ) -> (Array2<f32>, Array2<f32>, Array2<f32>) {
        let (input, z) = cache;
        let d_z = d_a * &self.activation.derivative(z);
        let d_w = input.t().dot(&d_z);
        let d_b = d_z.sum_axis(Axis(0)).insert_axis(Axis(0));
        let d_a_prev = d_z.dot(&self.weights.t());
        (d_a_prev, d_w, d_b)
    }
}

// Neural network structure
struct NeuralNetwork {
    layers: Vec<Layer>,
}

impl NeuralNetwork {
    fn new(layers: Vec<Layer>) -> Self {
        Self { layers }
    }

    // Training method
    fn train(&mut self, x: &Array2<f32>, y: &Array2<f32>, lr: f32, epochs: usize) {
        for epoch in 0..=epochs {
             // 1. FORWARD PASS: Compute predictions
            let mut caches = vec![];
            let mut a = x.clone();
            for layer in &self.layers {
                let (new_a, cache) = layer.forward(&a);
                a = new_a;
                caches.push(cache);
            }

            // 2. LOSS CALCULATION: Mean Squared Error
            let loss = ((&a - y).mapv(|x| x.powi(2))).mean().unwrap();

            // 3. BACKPROPAGATION: Compute gradients
            let mut d_a = 2.0 * (&a - y) / x.shape()[0] as f32; // Derivative of MSE
            for (i, layer) in self.layers.iter_mut().enumerate().rev() {
                let cache = &caches[i];

                // Compute parameter gradients
                let (d_a_prev, d_w, d_b) = layer.backward(&d_a, cache);
                
                // 4. GRADIENT DESCENT STEP: Update parameters
                // W = W - η * ∇W
                layer.weights = &layer.weights - (lr * d_w);
                // b = b - η * ∇b
                layer.biases = &layer.biases - (lr * d_b);
                
                // Propagate gradient to previous layer
                d_a = d_a_prev;
            }

            // Print progress
            if epoch % 1000 == 0 {
                println!("Epoch {:<5} | Loss: {:.4}", epoch, loss);
            }
        }
    }

    // Prediction method
    fn predict(&self, x: &Array2<f32>) -> Array2<f32> {
        let mut a = x.clone();
        for layer in &self.layers {
            let (new_a, _) = layer.forward(&a);
            a = new_a;
        }
        a
    }
}

fn main() {
    // XOR dataset
    let x = array![
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0]
    ];
    let p = array![
      [0.0, 1.0],
      [0.0, 0.0],
      [1.0, 0.0],
      [1.0, 1.0],
      [0.0, 0.0]
  ];
    let y = array![[0.0], [1.0], [1.0], [0.0]];

    // Create network with hidden layer (4 neurons)
    let mut nn = NeuralNetwork::new(vec![
        Layer::new(2, 4, Activation::ReLU),
        Layer::new(4, 1, Activation::Sigmoid),
    ]);

    // Train network
    nn.train(&x, &y, 0.1, 10000);

    // Get predictions
    let predictions = nn.predict(&p);
    println!("\nFinal predictions:");
    println!("{:.4}", predictions);
}