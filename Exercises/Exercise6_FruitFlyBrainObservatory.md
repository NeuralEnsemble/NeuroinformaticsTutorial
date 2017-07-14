# Exploring Brain Circuits with the Fruit Fly Brain Observatory

This file contains a few quick tutorial on how to get started exploring the fruit fly brain using the [Fruit Fly Brain Observatory](http://fruitflybrain.org/) platform. This tutorial contains the following sections:
- Exploratory Circuit Discovery with NeuroNLP
    - [Exercise 1-A: Access NeuroNLP and view the Demos](#exercis-1-a-access-neuronlp-and-view-the-demos)
    - [Exercise 1-B: Visualize Neurons in the Ellipsoid body](#exercise-1-b-visualize-neurons-in-the-ellipsoid-body)
    - [Exercise 1-C: Explore Fly Medulla Circuit from Janelia EM Data](#exercise-1-c-explore-fly-medulla-circuit-from-janelia-em-data)
    - [Exercise 1-D: Create and share a Tag](#exercise-1-d-create-and-share-a-tag)
    - [Exercise 1-E: Explore Networks from recent Publications](#exercise-1-e-explore-networks-from-recent-publications)
- Exploring Brain Circuit Function at Multiple Brain Levels
    - [Exercise 2-A: Exploring Whole-Brain Level Circuit](#exercise-2-a-exploring-whole-brain-level-circuit)  
    - [Exercise 2-B: Executing a Lamina Cartridge Circuit](#exercise-2-b-executing-a-lamina-cartridge-circuit)
- Digging Deeper

## Exploratory Circuit Discovery with NeuroNLP

This section contains a few demos on how to get started exploring the fruit fly brain with [NeuroNLP](https://neuronlp.fruitflybrain.org/), which is part of the [Fruit Fly Brain Observatory](http://fruitflybrain.org/) platform.

### Local software requirements

None, apart from an up to date web browser 

### Instructions

#### Exercise 1-A: Access NeuroNLP and View the Demos
 
1. Open up [NeuroNLP](https://neuronlp.fruitflybrain.org/).
2. Create and Account, or sign in as a Guest.
3. Either follow the Pop-Up to the Demo page, or you can find them yourself by Clicking on NeuroNLP, and finding 'Demos' in the drop down menu.
4. Find an interesting demo and click launch, the website will then automatically step through a series of queries that demonstrate how to use NeuroNLP.


#### Exercise 1-B: Visualize Neurons in the Ellipsoid body

NeuroNLP contains the morphologies of the [FlyCircuit Database](http://flycircuit.tw). This means we can easily visualize these neurons, and the primary way of starting this is looking at the neuropil level. We are going to start looking at the Ellipsoid Body.

    "Show neurons in the Ellipsoid Body"

   We can Investigate the FlyCircuit data source of a neuron by double clicking its body. By Hovering over the FlyCircuit DB menu in the top left hand corner, you can expand a panel which details the underlying neuron details, with further links to the Virtual Fly Brain where possible.

   From this point, we can start to explore the brain by adding and removing neurons, such as adding neurons that innervate the Ellipsoid body

    "Add neurons that innervate the EB"

   This will start to return a lot of neurons, when this is done, we might might want to reduce the number by only looking at the dopaminergic neurons in this set, using

    "Keep dopaminergic neurons"

There are lots of ways you can explore the data in NeuroNLP, check out the demos for more ways to slice and combine the data.


#### Exercise 1-C: Explore Fly Medulla Circuit from Janelia EM Data

NeuroNLP contains the detailed connectomic data of the [7 column medulla Electro-Microscopy (EM) data](https://github.com/janelia-flyem/ConnectomeHackathon2015) published by Janelia research campus. We can start out by visualizing all the Lamina neurons that innervate the Medulla in NeuroNLP

    "Show neurons in the Lamina"

Note that the data only contains the part of the neurons in the medulla. Therefore, currently, we can only visualize their axons in the Medulla.

We can look at the axons of the Lamina L1 neurons in the Medulla, using:

    "Show L1 neurons in the lamina"

Nevertheless we can start to see the columnar nature of the Lamina. We can further look at only a single cartridge in the lamina by using:

    "Show neurons in a single cartridge in the lamina"

We can also start to build up the flow of connectivity in the Lamina, by starting with a single L1 neuron.

    "Show L1 neurons in a single cartridge in the lamina"

As we are using the connectomic data, we can start to build up the circuit connectomically, by adding the postsynaptic Mi1 and Tm3 neurons:

    "Add postsynaptic neurons"

We can see a growing circuit of 14 neurons directly connected to the single L1 neuron. We can further run the same command, and build up the neurons 2 synaptic connections away, resulting in 246 neurons.
From here we can pull back to look at the L2 neurons using

    "Keep L2 neurons in a single cartridge"
   
And from here we can continue to explore the connectome, such as finding the neurons that synapse onto the L2 neurons:

    "Add presynaptic neurons"


#### Exercise 1-D: Create and share a Tag

After creating an interesting set of queries, you can Tag the results so that they can be easily shared and saved for later. To do this, click Create Tag at the top right, and enter a Tag Name such as "MyDemoTag". When you save this, you can reload the Tag using the Load tag button or share a link directly to the Tag using the link https://neuronlp.fruitflybrain.org/index.html?tag=MyDemoTag.

Currently, tags cannot be deleted or overwritten by any user. An error will be raised if you are creating a tag that has been previously defined.

We have used this tagging to create easily accessed links to circuits created from papers.

#### Exercise 1-E: Explore Networks from recent Publications

  In a recent paper by Sun Yi et. al., Neural signatures of dynamic stimulus selection in Drosophila, they describe a feedforward visual pathway from the medulla to the central complex. We can recreate and explore this network in NeuroNLP, by opening the following [10.1038/nn.4581](https://neuronlp.fruitflybrain.org/index.html?tag=10.1038/nn.4581) Tag.


## Exploring Brain Circuit Function at Multiple Levels

This section contains a few demos on how to explore executable brain circuits in [NeuroGFX](https://neurogfx.fruitflybrain.org/).


### Local software requirements

None, apart from an up to date web browser 

### Instructions

#### Exercise 2-A: Exploring Whole-Brain Level Circuit

Open up [NeuroGFX](https://neurogfx.fruitflybrain.org).

On this page you will see the whole-brain level circuit diagram of the fruit fly. Each block represents an Local Processing Unit (LPU) that is a model of a neuropil. A biological representation of the brain is shown in the small window on the top left. It can be enlarged by hovering the mouse onto the window. To swap the circuit diagram and the fly brain, simply double click on the small window.

Each LPU block is bound to its corresponding neuropil in the fly brain window. Clicking on an LPU will dim the block and remove the neuropil from the fly brain window.

You can also play with the "Toggle Neuropil" and "Toggle Track" menu in the top right corner.

#### Exercise 2-B: Executing a Lamina Cartridge Circuit

On the main NeuroGFX page, double click on the "LAM" block (for the Lamina Neuropil on the right eye). You will be taken to the Lamina LPU page. When it is loaded, double click on any of the cartridge (red circle).

Now you will see the circuit diagram of the Lamina cartridge. The morphology of the neurons is visualized in the small window in the top left corner of the screen. Click on the "Load Cartridge" button in the top right corner. This will initiate the communication with a NeuroArch server and load the model data of the cartridge circuit. The pop-up message will notify you when loading is complete.

You can check the model information by hovering on any of the neuron (orange block).  By clicking on the neurons, you can add/remove any neuron in the circuit. Once done, you can simulate the configured circuit by clicking on the "Open NK" button. This will start the simulation of the cartridge circuit with a (currently) predefined visual stimulus.

Once the simulation is finished, the activity of the neurons will be automatically visualized. 


## Digging Deeper

Details about the software architecture of FFBO and implementation of components are available [here](https://hackpad.com/Introduction-to-the-FFBO-Tutorials-alt48Yg7sUM).



