# Exploring Brain Circuits with the Fruit Fly Brain Observatory

This file contains a few quick tutorial on how to get started exploring the fruit fly brain using the [Fruit Fly Brain Observatory](http://fruitflybrain.org/) platform. This tutorial contains the following sections:
- Exploratory Circuit Discovery with NeuroNLP
    - [Exercise A: Access NeuroNLP and view the Demos](#Access-NeuroNLP-and-view-the-Demos)
    - [Exercise B: Visualize Neurons in the Ellipsoid body](#Visualize-Neurons-in-the-Ellipsoid-body)
    - [Exercise C: Explore Fly Medulla Circuit from Janelia EM Data](#Explore-Fly-Medulla-Circuit-from-Janelia-EM-Data)
    - [Exercise D: Create and share a Tag](#Create-and-share-a-Tag)
    - [Exercise E: Explore Networks from recent Publications](Explore-Networks-from-recent-Publications)
- Exploring Brain Circuit Function at Multiple Levels
    - [TODO]  

## Exploratory Circuit Discovery with NeuroNLP

This section contains a few demos on how to get started exploring the fruit fly brain with [NeuroNLP](https://neuronlp.fruitflybrain.org/), which is part of the [Fruit Fly Brain Observatory](http://fruitflybrain.org/) platform.

### Local software requirements

None, apart from an up to date web browser 

### Instructions

#### Access NeuroNLP and view the Demos
 
1. Open up [NeuroNLP](https://neuronlp.fruitflybrain.org/)
2. Create and Account, or sign in as a Guest.
3. Either follow the Pop-Up to the Demo page, or you can find them yourself by Clicking on NeuroNLP, and finding 'Demos' in the drop down menu.
4. Find an interesting demo and click launch, the website will then automatically step through a series of queries that demonstrate how to use NeuroNLP.


#### Visualize Neurons in the Ellipsoid body

NeuroNLP contains the morphologies of the Fly Circuit Database. This means we can easily visualize these neurons, and the primary way of starting this is looking at the neuropil level. We are going to start looking at the Ellipsoid Body.

    "Show neurons in the Ellipsoid Body"

   We can Investigate the  FlyCircuit data source of a neuron by double clicking its body. By Hovering over the FlyCircuit DB menu in the top left hand corner, you can expand a panel which details the underlying neuron details, with further links to the Virtual Fly Brain where possible.

   From this point, we can start to explore the brain by adding and removing neurons, such as adding neurons that innervate the Ellipsoid body

    "Add neurons that innervate the EB"

   This will start to return a lot of neurons, when this is done, we might might want to reduce the number by only looking at the dopaminergic neurons in this set, using

    "Keep dopaminergic neurons"

There are lots of ways you can explore the data in NeuroNLP, check out the demos for more ways to slice and combine the data.


#### Explore Fly Medulla Circuit from Janelia EM Data

NeuroNLP contains the detailed connectomic data of the [7 column medulla Electro-Microscopy (EM) data](https://github.com/janelia/connectomehackthon2015) published by Janelia research campus. We can start out by visualizing all the Lamina neurons that innervate the Medulla in NeuroNLP

    "Show neurons in the Lamina"

Note that the data only contains the part of the neurons in the medulla. Therefore, currently, we can only visualize their axons in the Medulla.

We can look at the axons of the Lamina L1 neurons in the Medulla, using:

    "Show L1 neurons in the lamina"

Nevertheless we can start to see the columnar nature of the Lamina. We can further look at only a single cartridge in the lamina by using:

    "Show neurons in a single cartridge in the lamina"

We can also start to build up the flow of connectivity in the Lamina, by starting with a single L1 neuron.

    "Show L1  neurons in a single cartridge in the lamina"

As we are using the connectomic data, we can start to build up the circuit connectomically, by adding the postsynaptic Mi1 and Tm3 neurons:

    "Add postsynaptic Mi1 neurons"
    "Add postsynaptic Tm3 neurons"

We can see a growing circuit of 13 neurons directly connected to the single L1 neuron. We can further run the same command, and build up the neurons 2 synaptic connections away, resulting in 246 neurons.
From here we can pull back to look at the L2 neurons using

    "Keep L2 neurons in a single cartridge"
   
And from here we can continue to explore the connectome, such as finding the neurons that synapse onto the L2 neurons:

    "Add presynaptic neurons"


#### Create and share a Tag

After creating an interesting set of queries, you can Tag the results so that they can be easily shared and saved for later. To do this, click Create Tag at the top right, and enter a Tag Name such as "MyDemoTag". When you save this, you can reload the Tag using the Load tag button or share a link directly to the Tag using the link https://neuronlp.fruitflybrain.org/index.html?tag=MyDemoTag.

We have used this tagging to create easily accessed links to circuits created from papers.

#### Explore Networks from recent Publications

  In a recent paper by Sun Yi et. al., Neural signatures of dynamic stimulus selection in Drosophila, they describe a feedforward visual pathway from the medulla to the central complex. We can recreate and explore this network in NeuroNLP, by opening the following [10.1038/nn.4581](https://neuronlp.fruitflybrain.org/index.html?tag=10.1038/nn.4581) Tag.


## Exploring Brain Circuit Function at Multiple Levels

This section contains a few demos on how to explore executable brain circuits in [NeuroGFX](https://neurogfx.fruitflybrain.org/).


<!-- ### Local software requirements

None, apart from an up to date web browser  -->

### Instructions


