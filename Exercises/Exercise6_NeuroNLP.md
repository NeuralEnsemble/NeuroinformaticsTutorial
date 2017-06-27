## Exploratory Circuit Discovery with NeuroNLP

This contains a quick tutorial on how to get started exploring the fruit fly brain with [NeuroNLP](https://neuronlp.fruitflybrain.org/), which is part of the [Fruit Fly Brain Observatory](http://fruitflybrain.org/) platform.

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


#### Explore the Lamina and build up a Cartridge model

NeuroNLP contains the detailed connectomic data of the visual system. We can start out by visualizing all the Lamina neurons in NeuroNLP

    "Show neurons in the Lamina"

We can look at the first layer of neurons in the lamina, the L1 neurons, using:

    "Show L1 neurons in the lamina"

Here we can start to see the columnar nature of the Lamina. We can further look at only a single cartridge in the lamina by using:

    "Show neurons in a single cartridge in the lamina"

We can also start to build up the flow of connectivity in the Lamina, by starting with a single L1 neuron.

    "Show L1  neurons in a single cartridge in the lamina"

As we are using the connectomic data, we can start to build up the circuit connectomically, by adding the post synaptic neurons:

    "Add post synaptic neurons"

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


