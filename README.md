<h2>Tecnologias Utilizadas</h2>
<ul>
    <li><strong>Linguagem:</strong> Python</li>
    <li><strong>Banco de Dados:</strong> SQLAlchemy como ORM</li>
    <li><strong>Banco de Dados Relacional:</strong> SQL</li>
</ul>

<h2>Funcionalidades</h2>
<h3>Cliente</h3>
<p><strong>Realizar Pedido (CRUD - Create):</strong> Permite que o cliente faça pedidos adicionando itens específicos e a quantidade desejada.</p>
<p><strong>Fluxo:</strong></p>
<ul>
    <li>O cliente visualiza os itens disponíveis.</li>
    <li>O cliente escolhe o item pelo ID e informa a quantidade desejada.</li>
    <li>O pedido é salvo no sistema associado ao nome do cliente.</li>
</ul>

<p><strong>Consultar Pedido (CRUD - Read):</strong> O cliente pode consultar um pedido específico pelo nome para verificar os itens associados.</p>
<p><strong>Fluxo:</strong></p>
<ul>
    <li>O cliente insere o nome do pedido.</li>
    <li>O sistema verifica se o pedido existe e exibe os detalhes.</li>
</ul>

<p><strong>Excluir Pedido (CRUD - Delete):</strong> Permite que o cliente exclua um pedido específico pelo ID.</p>
<p><strong>Fluxo:</strong></p>
<ul>
    <li>O cliente visualiza todos os pedidos associados a ele.</li>
    <li>O cliente escolhe qual pedido deseja excluir inserindo o ID.</li>
</ul>

<p><strong>Atualizar Pedido (CRUD - Update):</strong> Permite que o cliente atualize a quantidade ou o item em um pedido existente.</p>
<p><strong>Fluxo:</strong></p>
<ul>
    <li>O cliente visualiza seus pedidos e escolhe qual pedido deseja atualizar e insere o ID.</li>
    <li>Atualiza o item e a quantidade conforme necessário.</li>
</ul>

<h3>Colaborador</h3>
<p><strong>Cadastrar (CRUD - Create):</strong> Permite o cadastro de novos clientes, colaboradores e itens.</p>
<p><strong>Fluxo:</strong></p>
<ul>
    <li>O colaborador preenche os detalhes do cliente, colaborador ou item.</li>
    <li>O sistema salva no banco de dados.</li>
</ul>

<p><strong>Atualizar (CRUD - Update):</strong> Permite que o colaborador atualize informações de clientes, colaboradores ou itens.</p>
<p><strong>Fluxo:</strong></p>
<ul>
    <li>O colaborador visualiza o cadastro atual.</li>
    <li>Escolhe qual cadastro deseja atualizar e insere as novas informações.</li>
</ul>

<h2>UML</h2>
<p><em>Diagrama de classes UML e outros detalhes gráficos serão adicionados para representar visualmente os relacionamentos e fluxos do sistema.</em></p>

<hr>
<p>Este projeto oferece um sistema robusto e eficiente para gerenciar todos os aspectos de pedidos e cadastros, facilitando a gestão tanto para clientes quanto para colaboradores.</p>
