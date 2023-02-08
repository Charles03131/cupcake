

const BASE_URL="http://localhost:5000/api";


// GENERATE CUPCAKE HTML WITH GIVEN DATA


function makeCupcakeHTML(new_cupcake){
    
 return `
   <div data-cupcake-id="${new_cupcake.id}">
    
   <li>
   ${new_cupcake.flavor}/${new_cupcake.size}/${new_cupcake.rating}
    </li>
        <img class="cupcake-img" src="${new_cupcake.image}" alt="(no image provided)">
       
        <buttond>X</button>

    </div>
    `;
}



//show initial cupcakes on page


async function add_cupcakes(){
    const response=await axios.get(`${BASE_URL}/cupcakes`);

    for(let cupcakeData of response.data.cupcakes){
        let newCupcake=$(makeCupcakeHTML(cupcakeData));
        $("#cupcakes-list").append(newCupcake);
    }
}



//handle form for adding of new cupcakes


$("#new-cupcake-form").on("submit", async function (evt){
    evt.preventDefault();

    
    let flavor=$("#flavor").val();
    let size=$("#size").val();
    let rating=$("#rating").val();
    let image=$("#image").val();

    const newCupcakeResponse=await axios.post(`${BASE_URL}/cupcakes`,{
      flavor,rating,size,image
    });

    let newCupcake=$(makeCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("new-cupcake-form").trigger("reset");
});



// DELETING A CUPCAKE 
$(".delete_cupcake").click(deleteCupcake)

async function deleteCupcake(){
   const id=$(this).data('id');
   await axios.delete(`/api/cupcakes/${id}`)
   $(this).parent().remove()
}


